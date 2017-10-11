from rest_framework import serializers
from ..models import JointExam


class JointExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = JointExam
        fields = '__all__'


class JointExamRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = JointExam
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class JointExamDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = JointExam
        exclude = ('id', 'is_active', 'updated_by',
                   'created_by', 'created_on', 'updated_on', 'patient_encounter',
                   'encounter_id',
                   )
