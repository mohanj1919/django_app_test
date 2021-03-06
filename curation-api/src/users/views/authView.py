import logging

from datetime import datetime, timezone

import boto3
from django.conf import settings
from django.contrib.auth.models import Group
from rest_framework import permissions, serializers, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from ...patients.models import AdminSetting, EmailTemplate
from ..auth_backend import EmailBackend
from ..models import CurationUser
from ..serializers import LoginSerializer, MfaSerializer, ResetPasswordSerializer, UserSerializer
from ..serializers.userSerializer import get_password_expiry_cycle_days, can_update_user_password
from ..utils import SendEmailUtil, get_totp_instance

# Get an instance of a logger
logger = logging.getLogger(__name__)

class AuthViewSet(viewsets.GenericViewSet):
    """
    Enpoints for managing User Authentication
    """
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)

    def get_serializer_class(self):
        if self.action == 'reset_password':
            return ResetPasswordSerializer
        return LoginSerializer

    def _create_auth_token(self, user=None):
        """
        Creates api Token for the authenticated user
        """
        token, created = Token.objects.get_or_create(user=user)
        return token

    def _get_mfa_uri(self, email, secret):
        """
        Returns the MFA URI compatible with Google Authenticator
        """
        totpInstance = get_totp_instance(secret)
        provider = settings.PROVIDER_NAME
        provisioning_uri = totpInstance.provisioning_uri(
            name=email, issuer_name=provider)
        return provisioning_uri

    def _authenticate_and_get_user(self, email, password, user=None):
        """
        Authenticates and returns the user if valid
        """
        # Authenticate the user
        emailBackend = EmailBackend()
        user = emailBackend.authenticate(username=email, password=password, user=user)
        return user

    def is_password_expired(self, user):
        if user.password_expiry_on is not None and datetime.now(timezone.utc) > user.password_expiry_on:
            return True
        else:
            return False

    def send_otp_message(self, otp_secret_key, phone_number):
        totp_instance = get_totp_instance(otp_secret_key, interval=60)
        msg = AdminSetting.objects.get_setting_value(
            AdminSetting.ConfigurableSettings.otp_message, settings.OTP_MESSAGE)
        msg = msg.format(otp=totp_instance.now())
        logger.info('Sending OTP message: "%s" to "%s"', msg, phone_number)
        try:
            # Create an SNS client
            client = boto3.client(
                "sns",
                aws_access_key_id=settings.DJANGO_AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.DJANGO_AWS_SECRET_ACCESS_KEY,
                region_name=settings.DJANGO_AWS_REGION
            )
            client.publish(PhoneNumber=phone_number, Message=msg)
        except:
            logger.error('Failed to Send the OTP message')
        return

    def check_user_exists(self, email):
        user = CurationUser.objects.get(email__iexact=email.lower())
        if user is not None and user.is_deleted:
            res = {'message': 'User details not found'}
            return Response({'message': 'User details not found'}, status=status.HTTP_404_NOT_FOUND)

    @list_route(methods=['post'])
    def login(self, request):
        """
        Validate user credentials
        """
        credentials = request.data
        serializer = LoginSerializer(data=credentials)
        serializer.is_valid(raise_exception=True)

        try:
            user = EmailBackend().get_user(credentials['email'])
        except:
            return Response({"message": "User details not found."}, status=status.HTTP_401_UNAUTHORIZED)

        user = self._authenticate_and_get_user(credentials['email'], credentials['password'], user=user)

        if user is None:
            return Response({"message": "Your username and password didn't match."}, status=status.HTTP_401_UNAUTHORIZED)

        if self.is_password_expired(user):
            res = {
                "message": "Password expired. Please reset your password.",
                "password_expired": True
            }
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)

        resData = {
            "message": "Successfully authenticated",
            "password_expiry_on": user.password_expiry_on,
            "mfa_type": user.mfa_type
        }

        if not user.require_mfa:
            token = self._create_auth_token(user)
            resData['api_token'] = str(token)

        phone_number_last_4_digits = None

        if user.require_mfa and user.mfa_type == CurationUser.MfaType.sms and user.phone_number is not None:
            phone_number_last_4_digits = '{message:{fill}{align}{width}}'.format(
                message=user.phone_number[-4:], fill='*', align='>', width=len(user.phone_number))
            resData['phone_number'] = phone_number_last_4_digits
            otp_secret_key = user.otp_secret_key
            self.send_otp_message(otp_secret_key, user.phone_number)

        return Response(resData, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def verify_mfa_token(self, request):
        """
        Verifies the MFA token
        returns the user detials and api_token if valid
        """
        credentials = request.data
        serializer = MfaSerializer(data=credentials)
        serializer.is_valid(raise_exception=True)

        try:
            user = EmailBackend().get_user(credentials['email'])
        except:
            return Response({"message": "User details not found."}, status=status.HTTP_401_UNAUTHORIZED)

        user = self._authenticate_and_get_user(credentials['email'], credentials['password'], user)

        if user is None:
            return Response({"message": "Your username and password didn't match."}, status=status.HTTP_401_UNAUTHORIZED)

        if self.is_password_expired(user):
            res = {
                "message": "Password expired. Please reset your password.",
                "password_expired": True
            }
            return Response(res, status=status.HTTP_401_UNAUTHORIZED)

        otp_secret_key = user.otp_secret_key

        if user.require_mfa and user.mfa_type == CurationUser.MfaType.sms:
            totp_instance = get_totp_instance(otp_secret_key, interval=60)
        elif user.require_mfa and user.mfa_type == CurationUser.MfaType.google:
            totp_instance = get_totp_instance(otp_secret_key)
        else:
            totp_instance = None

        if totp_instance is not None and not totp_instance.verify(credentials['token']):
            return Response({
                "error": "Invalid token provided"
            })

        userSerializer = UserSerializer(user)
        token = self._create_auth_token(user)
        response = {
            "user": userSerializer.data,
            "api_token": str(token)
        }
        return Response(response, status=status.HTTP_200_OK)

    @list_route(methods=['post'])
    def reset_password(self, request):
        """
        Reset the password for the user
        """
        password = request.data['password']
        forgot_password_hash = request.data['uuid']
        url_expired_response = Response(
            {"message": 'Password reset url expired'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CurationUser.objects.get(
                forgot_password_hash=forgot_password_hash)

            # get pwd_expiry_cycle_days value from admin_settings table
            pwd_expiry_cycle_days = get_password_expiry_cycle_days()

            if user is None:
                return url_expired_response
            if user.forgot_password_hash_expiry_on.isoformat() < datetime.now().isoformat():
                return url_expired_response

            successs_response = {
                "message": "password set successfully"
            }

            mfaUrl = self._get_mfa_uri(user.email, user.otp_secret_key)

            if (not user.is_active and user.mfa_type == CurationUser.MfaType.google) or user.is_staff:
                successs_response["mfaUrl"] = mfaUrl

            # if password reset is requrested by admin then reset the otp secret key and return mfa_url
            if user.reset_password_requested_by is not None:
                reset_password_requested_by = UserSerializer(
                    user.reset_password_requested_by).data
                reset_password_requested_by_user_group = reset_password_requested_by.get('groups')[0]
                admin_group = Group.objects.get(name='admin')

                if admin_group is not None \
                        and admin_group.name == reset_password_requested_by_user_group.get('name') \
                        and user.mfa_type == CurationUser.MfaType.google:
                    successs_response["mfaUrl"] = mfaUrl

            if can_update_user_password(user, password):
                user.update_password(password, pwd_expiry_cycle_days)
                user.is_active = True
                user.reset_password_requested_by = None
                user.forgot_password_hash = None
                user.forgot_password_hash_expiry_on = None
                return Response(successs_response, status=status.HTTP_200_OK)
            else:
                error_response = {'errors': {}}
                error_response['errors']['new_password'] = ["Password already used before."]
                raise serializers.ValidationError(error_response)
        except CurationUser.DoesNotExist:
            return url_expired_response
        except ValidationError as err:
            raise err
        except:
            return Response({"message": "Unable to reset password"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @list_route()
    def forgot_password(self, request):
        mail_id = request.GET['email']
        try:
            user = CurationUser.objects.get(email=mail_id, is_deleted=False, is_account_locked=False)
            SendEmailUtil().generate_reset_password_link(user, EmailTemplate.Templates.reset_password_email)
            return Response({"message": "forgot password email sent"}, status=status.HTTP_200_OK)
        except CurationUser.DoesNotExist:
            return Response({"message": "user details not found with this email"}, status=status.HTTP_404_NOT_FOUND)
