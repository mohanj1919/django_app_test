from django.test import TestCase
from rest_framework import serializers

from ...serializers.admin_settings import AdminSettingSerializer


class TestAdminSettingsSerializer(TestCase):

    def test_create_admin_setting(self):
        admin_setting = [{
            "setting": "Some setting", "text": "some text",
            "type": "text", "value": 'some value',
            "min": 10, "max": 200, "settings_group": 'setting'
        }]
        serializer = AdminSettingSerializer(data=admin_setting, many=True)
        is_valid = serializer.is_valid()
        self.assertEqual(is_valid, True)

    def test_create_invalid_admin_setting(self):
        invalid_admin_setting = [{
            "setting": "Some setting", "text": "some text",
            "type": "text", "value": '',
            "min": 10, "max": 200, "settings_group": 'setting'
        }]
        serializer = AdminSettingSerializer(
            data=invalid_admin_setting, many=True)
        is_valid = serializer.is_valid()
        self.assertEqual(is_valid, False)

    def test_validate_setting_value_first_case(self):
        admin_setting = {
            "setting": "Some setting", "text": "some text",
            "type": "number", "value": '5',
            "min": 10, "max": 200, "settings_group": 'setting'
        }
        try:
            AdminSettingSerializer().validate_setting_value(
                admin_setting['min'],
                admin_setting['max'],
                admin_setting['setting'],
                admin_setting['text'],
                admin_setting['type'],
                admin_setting['value'])
        except serializers.ValidationError as er:
            message = 'value must be between {min} and {max}'
            assert_err = {"errors": {}}
            assert_err['errors'][admin_setting['setting']] = [message.format(
                min=admin_setting['min'], max=admin_setting['max'])]
            self.assertEqual(er.detail, assert_err)

    def test_validate_setting_value_second_case(self):
        admin_setting = {
            "setting": "Some setting", "text": "some text",
            "type": "number", "value": 'some val',
            "min": 10, "max": 200, "settings_group": 'setting'
        }
        try:
            AdminSettingSerializer().validate_setting_value(
                admin_setting['min'],
                admin_setting['max'],
                admin_setting['setting'],
                admin_setting['text'],
                admin_setting['type'],
                admin_setting['value'])
        except serializers.ValidationError as er:
            response = {"errors": {}}
            message = 'please provide valid value'
            response["errors"][admin_setting['setting']] = [message]
            our_error = serializers.ValidationError(response)
            self.assertEqual(response, er.detail)

    def test_validate_setting_value_third_case(self):
        admin_setting = {
            "setting": "Some setting", "text": "some text",
            "type": "text", "value": 'some',
            "min": 10, "max": 200, "settings_group": 'setting'
        }
        try:
            AdminSettingSerializer().validate_setting_value(
                admin_setting['min'],
                admin_setting['max'],
                admin_setting['setting'],
                admin_setting['text'],
                admin_setting['type'],
                admin_setting['value'])
        except serializers.ValidationError as er:
            response = {"errors": {}}
            message = 'value must be less than {max} characters'
            message = message.format(max=admin_setting['max'])
            response["errors"][admin_setting['setting']] = [message]
            our_error = serializers.ValidationError(response)
            self.assertEqual(response, er.detail)
