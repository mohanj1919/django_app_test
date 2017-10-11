from rest_framework import serializers

from ..models import Medication, Provider


class MedicationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationRecordRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        exclude = ('updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter')


class MedicationRecordDataSerializer(serializers.ModelSerializer):
    NDC = serializers.SerializerMethodField()
    GPI = serializers.SerializerMethodField()
    DAW = serializers.SerializerMethodField('get_daw_flag')
    Days_Supply_Calculated = serializers.SerializerMethodField()
    Doses_Per_Day_Calculated = serializers.SerializerMethodField()
    Refills_Authorized = serializers.SerializerMethodField()
    documenting_provider_speciality = serializers.SerializerMethodField()
    administering_provider_speciality = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    discontinued = serializers.SerializerMethodField()
    prescribing_provider_speciality = serializers.SerializerMethodField()

    def get_NDC(self, instance):
        return instance.ndc

    def get_GPI(self, instance):
        return instance.gpi

    def get_Days_Supply_Calculated(self, instance):
        return instance.days_supply_derived

    def get_Doses_Per_Day_Calculated(self, instance):
        return instance.doses_per_day_derived

    def get_Refills_Authorized(self, instance):
        return instance.refills_authorized_numeric

    def get_documenting_provider_speciality(self, instance):
        return Provider().get_speciality(instance.documenting_provider_id)

    def get_administering_provider_speciality(self, instance):
        return Provider().get_speciality(instance.administering_provider_id)

    def get_prescribing_provider_speciality(self, instance):
        return Provider().get_speciality(instance.prescribing_provider_id)

    def get_name(self, instance):
        return instance.name

    def get_bool_response(self, value):
        if value is None:
            return None
        if value == "true":
            return "Yes"
        elif value == "false":
            return "No"

    def get_discontinued(self, instance):
        return self.get_bool_response(instance.discontinued)

    def get_daw_flag(self, instance):
        return self.get_bool_response(instance.daw_flag)

    class Meta:
        model = Medication
        exclude = ('id', 'is_active', 'documenting_provider_id', 'gpi', 'refills_authorized_numeric', 'doses_per_day_derived',
                   'days_supply_derived', 'ndc', 'updated_by', 'created_by', 'created_on', 'updated_on', 'patient_encounter',
                   'encounter_id', 'daw_flag', 'infusion_flag', 'administering_provider_id', 'expire', 'or_dispense',
                   'expire_dttm', 'infusion_end_dttm', 'infusion_expiry_1_dttm', 'end' , 'pharmacy_prescription_id', 'code',
                   'infusion_expiry_2_dttm', 'infusion_expiry_3_dttm', 'infusion_expiry_4_dttm', 'infusion_start_dttm', 'start_dttm',
                   'discontinued', 'documenting_prov_id', 'prescribing_provider_id'
                   )
