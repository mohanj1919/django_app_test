from rest_framework import serializers
from ..models import Note, Provider


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class NoteDataSerializer(serializers.ModelSerializer):
    documenting_provider_speciality = serializers.SerializerMethodField('get_speciality')

    class Meta:
        model = Note
        exclude = ('id', 'is_active', 'documenting_provider_id', 'updated_by',
                   'created_by', 'created_on', 'updated_on', 'patient_encounter',
                   'encounter_id',
                   )

    def get_speciality(self, instance):
        return Provider().get_speciality(instance.documenting_provider_id)
