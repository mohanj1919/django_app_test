from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ....users.models import CurationUser, CurationUserManager
from ...models import CRFQuestion
from ...serializers import CRFQuestionSerializer


class TestCrfQuestion(TestCase):
    def setUp(self):
        admin = CurationUser.objects.get(email='mohan.jagabatthula@ggktech.com')
        self.client = APIClient()
        self.client.force_authenticate(user=admin)
        self.crf_question1=CRFQuestion.objects.create(text ='some text',
            description ='some description',
            type = 'some type',
            responses ='responses',
            note='our note')
        self.crf_question2=CRFQuestion.objects.create(text ='some text2',
            description ='some description',
            type = 'some type',
            responses ='responses',
            note='our note')
        self.crf_question3=CRFQuestion.objects.create(text ='some text3',
            description ='some description',
            type = 'some type',
            responses ='responses',
            note='our note')

        self.valid_crfquestion_input={
            'text': 'some text4',
            'description' :'some description',
            'type' : 'some type',
            'responses' :'responses',
            'note':'our note'
        }

        self.invalid_crfquestion_input={
            'text': 'some text5',
            'description' :'some description',
            'type' : '',
            'responses' :'responses',
            'note':'our note'
        }
        self.valid_crfquestion_update={
            'text': 'some text6',
            'description' :'some description',
            'type' : 'some type',
            'responses' :'responses',
            'note':'our note'
        }

    def test_get_crf_questions(self):
        url = '/clinical/crfquestions/'
        response = self.client.get(url)
        crf_questions = CRFQuestion.objects.all()
        serializer =CRFQuestionSerializer(crf_questions, many=True)
        #self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_crf_questions_with_id(self):
        url = '/clinical/crfquestions/{id}/'.format(
            id=self.crf_question1.id
        )
        response=self.client.get(url)
        crf_question=CRFQuestion.objects.get(text='some text')
        serializer =CRFQuestionSerializer(crf_question)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_get_invalid_crf_question(self):
    #     url = '/clinical/crfquestions/{id}/'.format(
    #         id=self.crf_question1.id
    #     )
    #     response=self.client.get(url)
    #     crf_question=CRFQuestion.objects.get(text='123t')
    #     serializer =CRFQuestionSerializer(crf_question)

    def test_post_a_crf_question(self):
        url = '/clinical/crfquestions/'
        response=self.client.post(url,data=self.valid_crfquestion_input,format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_an_invalid_crf_question(self):
        url = '/clinical/crfquestions/'
        response=self.client.post(url,data=self.invalid_crfquestion_input,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)

    def test_update_a_crf_question(self):
        url = '/clinical/crfquestions/{id}/'.format(
            id=self.crf_question1.id
        )
        response=self.client.put(url,data=self.valid_crfquestion_update,format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_update_an_invalid_crf_question(self):
        url = '/clinical/crfquestions/{id}/'.format(
            id=self.crf_question1.id
        )
        response=self.client.put(url,data=self.invalid_crfquestion_input,format='json')
        self.assertEqual(response.status_code,status.HTTP_400_BAD_REQUEST)
