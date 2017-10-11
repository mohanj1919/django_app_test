from rest_framework import serializers
from ..models import Provider


class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'


class ProviderDataSerializer(serializers.ModelSerializer):
    NPI = serializers.SerializerMethodField()

    def get_NPI(self, instance):
        return instance.npi

    class Meta:
        model = Provider
        exclude = ('id', 'is_active', 'updated_on', 'created_on',
                   'created_by', 'updated_by', 'cohort', 'npi', 'provider_id')
