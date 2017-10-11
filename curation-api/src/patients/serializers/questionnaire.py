from rest_framework import serializers
from ..models import Questionnaire


class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        fields = '__all__'


class QuestionnaireRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class QuestionnaireDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionnaire
        exclude = ('id', 'is_active', 'updated_by',
                   'created_by', 'created_on', 'updated_on', 'patient_encounter',
                #    'encounter_id',
                   )
