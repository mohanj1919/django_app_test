from rest_framework import serializers
from ..models import Procedure, Provider


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = '__all__'


class ProcedureRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class ProcedureDataSerializer(serializers.ModelSerializer):
    billing_provider_speciality = serializers.SerializerMethodField()
    ordering_provider_speciality = serializers.SerializerMethodField()
    performing_provider_speciality = serializers.SerializerMethodField()
    
    def get_performing_provider_speciality(self, instance):
        return Provider().get_speciality(instance.performing_provider_id)

    def get_ordering_provider_speciality(self, instance):
        return Provider().get_speciality(instance.ordering_provider_id)

    def get_billing_provider_speciality(self, instance):
        return Provider().get_speciality(instance.billing_provider_id)

    class Meta:
        model = Procedure
        exclude = ('id', 'is_active', 'encounter_id', 'updated_by',
                   'created_by', 'created_on', 'updated_on', 'patient_encounter',
                    'billing_provider_id', 'ordering_provider_id', 'performing_provider_id'
                   )
