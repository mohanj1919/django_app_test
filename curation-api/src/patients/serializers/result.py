from rest_framework import serializers
from ..models import Result


class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'


class ResultRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class ResultDataSerializer(serializers.ModelSerializer):
    abnormal = serializers.SerializerMethodField()

    def get_bool_response(self, value):
        if value is None:
            return None
        if value == "true":
            return "Yes"
        elif value == "false":
            return "No"

    def get_abnormal(self, instance):
        return self.get_bool_response(instance.abnormal)
    
    class Meta:
        model = Result
        exclude = ('id', 'is_active', 'updated_by',
                   'created_by', 'created_on', 'updated_on', 'patient_encounter',
                    'encounter_id',
                   )
