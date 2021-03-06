from django.db import transaction
from django.db.models import Q
from django.http import Http404
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from rest_framework.exceptions import ValidationError

from ...utilities import ListModelViewMixin, GenericViewSet
from ..models import CRFTemplateQuestion, CRFTemplate, PatientChartReview
from ..serializers import (
    CRFTemplateListSerializer,
    CRFTemplateQuestionListSerializer,
    CRFTemplateQuestionSerializer,
    CRFTemplateSerializer,
    CRFTemplateRetrieveSerializer
)


class CRFTemplateView(GenericViewSet,
                      ListModelViewMixin):
    queryset = CRFTemplate.objects.filter(is_active=True)
    permission_classes = (permissions.IsAuthenticated,)
    model = CRFTemplate
    curator_allowed_actions = ['retrieve']

    def _get_object(self, pk):
        try:
            return CRFTemplate.objects.get(pk=pk)
        except CRFTemplate.DoesNotExist:
            raise Http404

    def _get_crf_tempalte_question(self, pk):
        try:
            return CRFTemplateQuestion.objects.get(pk=pk)
        except CRFTemplateQuestion.DoesNotExist:
            raise Http404

    def get_serializer_class(self):
        if self.action in ['create', 'update']:
            return CRFTemplateSerializer
        if self.action == 'retrieve':
            return CRFTemplateRetrieveSerializer
        return CRFTemplateListSerializer

    def filter_query_set(self, search_param):
        query = Q(name__icontains=search_param) | Q(description__icontains=search_param)
        return self.get_queryset().filter(query)

    def retrieve(self, request, pk=None):
        crf_template = self._get_object(pk)
        serializer = self.get_serializer(crf_template)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def _create_crf_template_question(self, crf_template_id, questions_to_insert):
        questions = []

        for question in questions_to_insert:
            question['crf_template_id'] = crf_template_id
            question_serializer = CRFTemplateQuestionSerializer(data=question)

            if not question_serializer.is_valid():
                raise ValidationError({'errors': question_serializer.errors})

            crfQuestion = question_serializer.save()
            crfQuestion = CRFTemplateQuestionListSerializer(crfQuestion)
            questions.append(crfQuestion.data)
        return questions

    def _update_crf_template_question(self, questions_to_update):
        questions = []

        for question in questions_to_update:
            question_id = question.get('id')
            question_instance = self._get_crf_tempalte_question(question_id)
            question_serializer = CRFTemplateQuestionSerializer(question_instance, data=question)
            if not question_serializer.is_valid():
                raise ValidationError({'errors': question_serializer.errors})

            crf_question = question_serializer.save()
            # if a question is deleted (is_active=False) then update the child questions
            if not question.get('is_active', True):
                child_questions = CRFTemplateQuestion.objects.filter(
                    parent_question=question_instance.question_id,
                    is_active=True)
                child_questions.update(parent_question='', parent_condition='', parent_response='')
            crf_question_serializer = CRFTemplateQuestionListSerializer(crf_question)
            questions.append(crf_question_serializer.data)
        return questions

    @transaction.atomic
    def create(self, request):
        data = request.data
        serializer = CRFTemplateSerializer(data=data)
        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        created_template = serializer.save()
        questions_to_insert = data.get('questions')

        try:
            questions = self._create_crf_template_question(created_template.id, questions_to_insert)
        except ValidationError as validation_error:
            raise validation_error

        obj = serializer.data
        obj['questions'] = questions
        return Response(obj, status=status.HTTP_201_CREATED)

    def _delete_crf_template_questions(self, questions_to_be_deleted):
        for question in questions_to_be_deleted:
            question['is_active'] = False

        response = self._update_crf_template_question(questions_to_be_deleted)
        return response

    @transaction.atomic
    def update(self, requests, pk=None):
        data = requests.data
        instance = self._get_object(pk)
        serializer = CRFTemplateSerializer(instance, data=data)

        if not serializer.is_valid():
            return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        patient_chart_reviews = PatientChartReview.objects.filter(
            status__in=[
                PatientChartReview.StatusType.inprogress,
                PatientChartReview.StatusType.completed],
            crf_template_id=instance.id).distinct('crf_template_id')

        if patient_chart_reviews:
            message = "Unable to edit CRF '{}'. Template is used in active project.".format(instance.name)
            res = {'errors': message}
            return Response(res)

        updated_template = serializer.save()
        crfTemplateSerializer = CRFTemplateListSerializer(updated_template)
        questions = []

        questions_in_req = data.get('questions')
        questions_to_update = []
        questions_to_insert = []

        for question in questions_in_req:
            crf_tempalte_id = instance.id
            question_id = question.get('question_id')
            try:
                crf_template_question = CRFTemplateQuestion.objects.get(
                    crf_template_id=instance.id, 
                    question_id=question_id)
                question['id'] = crf_template_question.id
                questions_to_update.append(question)
            except CRFTemplateQuestion.DoesNotExist as er:
                questions_to_insert.append(question)

        try:
            self._create_crf_template_question(instance.id, questions_to_insert)
        except ValidationError as validation_error:
            raise validation_error

        try:
            self._update_crf_template_question(questions_to_update)
        except ValidationError as validation_error:
            raise validation_error

        crf_template_questions = CRFTemplateQuestion.objects.filter(crf_template_id=instance.id, is_active=True)
        questions = CRFTemplateQuestionListSerializer(crf_template_questions, many=True).data

        obj = crfTemplateSerializer.data
        obj['questions'] = questions
        return Response(obj, status=status.HTTP_200_OK)

    @transaction.atomic
    def destroy(self, request, pk=None):
        instance = self._get_object(pk)
        instance.is_active = False
        patient_chart_reviews = PatientChartReview.objects.filter(
            status__in=[
                PatientChartReview.StatusType.inprogress,
                PatientChartReview.StatusType.completed],
            crf_template_id=instance.id).distinct('crf_template_id')
        if patient_chart_reviews:
            message = "Cannot delete crf template '{}' which is involved in patient curation.".format(instance.name)
            res = {'errors': {}}
            res['errors']['crf_templates'] = [message]
            raise ValidationError(res)
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
