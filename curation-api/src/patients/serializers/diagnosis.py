from rest_framework import serializers
from ..models import Diagnosis


class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('__all__')


class DiagnosisRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        exclude = ('updated_by', 'created_by', 'created_on',
                   'updated_on', 'patient_encounter',)


class DiagnosisDataSerializer(serializers.ModelSerializer):
    principal = serializers.SerializerMethodField()

    def get_bool_response(self, value):
        if value is None:
            return None
        if value == "true":
            return "Yes"
        elif value == "false":
            return "No"

    def get_principal(self, instance):
        return self.get_bool_response(instance.principal_dx)

    class Meta:
        model = Diagnosis
        exclude = ('id', 'is_active', 'updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter',
                   'encounter_id', 'principal_dx',
                   )
