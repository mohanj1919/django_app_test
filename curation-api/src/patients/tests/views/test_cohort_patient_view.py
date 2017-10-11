from json import loads, dumps
from collections import OrderedDict
from django.conf import settings
from django.contrib.auth.models import Group
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import Group
from rest_framework.request import Request
from rest_framework.authtoken.models import Token
from ....users.models import CurationUser, CurationUserManager
#from ..serializers.userSerializer import CreateUserSerializer, UserSerializer, GroupSerializer
#from ..views.userView import UserViewSet
from ...models.patient import Patient
from ...models.cohort import Cohort
from ...models.appointment import Appointment
from ...serializers.appointment import AppointmentSerializer
from ...models import Patient, ProjectCohortPatient
from ...serializers import PatientSerializer
from ...serializers.patient import PatientListSerializer

valid_patient_input1 = {
    "patient_id": "4dbe5c7d-a03c-3a44-9245-7233fa0dcba5",
    "deceased": "No deceased indicator present",
    "race": "White",
    "sex_at_birth": "Female",
    "date_of_birth": 1958,
    "dob_is_year": True,
    "encounters": [
        {
            "data_source_id": 5,
            "provider_id": "2D171E61-2B5A-7854-8569-7FD458746EE2",
            "id": "31934984-5F98-4ADB-804E-DB9E94185183",
            "start": "2014-01-13 08:45:00",
            "end": None,
            "admitting_provider_id": None,
            "rendering_provider_id": "CSC:334E678F-D256-4B9D-BFBF-224455D90684",
            "facility_id": "CSC:9D971E61-2B5A-4504-9016-7FD863790EE2",
            "discharge_disposition": None,
            "place_of_service": None,
            "type": "Ambulatory Services Encounter",
            "type_of_bill": None,
            "diagnoses": [
                {
                    "id": None,
                    "code": "338.4",
                    "code_type": "ICD9_Diagnosis",
                    "name": None,
                    "category": "Patient diagnosis",
                    "status": None,
                    "onset": None,
                    "resolution": None,
                    "principal_dx": None
                },
            ],
            "joint_exams": [],
            "medications": [
                {
                    "id": None,
                    "medication_record_type": "order",
                    "administering_provider_id": None,
                    "action": "Medication prescription to patient or pharmacy",
                    "code": None,
                    "dispense_as_written": None,
                    "days_supply": None,
                    "days_supply_derived": None,
                    "discontinued": None,
                    "dispense_quantity": "120",
                    "doses_per_day": None,
                    "doses_per_day_derived": None,
                    "end": "2014-02-11 00:00:00",
                    "expire": None,
                    "form": None,
                    "frequency": None,
                    "gpi": None,
                    "infusion_dose": None,
                    "infusion_end": None,
                    "infusion_expiry_1": None,
                    "infusion_expiry_2": None,
                    "infusion_expiry_3": None,
                    "infusion_expiry_4": None,
                    "infusion": None,
                    "infusion_patient_weight": None,
                    "infusion_patient_weight_unit": None,
                    "infusion_planned_dose": None,
                    "infusion_planned_dose_unit": None,
                    "infusion_rate": None,
                    "infusion_rate_unit": None,
                    "infusion_reason_for_adjustment": None,
                    "infusion_start": None,
                    "infusion_therapy_type": None,
                    "infusion_volume_infused": None,
                    "infusion_volume_infused_unit": None,
                    "name": "oxycodone 20 mg tablet",
                    "ndc": "10702005701",
                    "or_dispense": None,
                    "pharmacy_fill_number": None,
                    "prescription_fill_number": None,
                    "reason_for_discontinuation": None,
                    "reason_for_start": None,
                    "refills_authorized": "0",
                    "refills_authorized_numeric": None,
                    "route_of_admin": None,
                    "rxnorm": None,
                    "sig": "take 1 tablet by oral route  every 6 hours",
                    "start": "2014-01-13 00:00:00",
                    "status": None,
                    "strength": "20",
                    "total_dose": None,
                    "type": None,
                    "unit": "mg"
                }
            ],
            "notes": [
                {
                    "id": None,
                    "name": "history_of_present_illness",
                    "documenting_provider_id": None,
                    "text": "Severity level is 8.  It occurs persistently and is without change."
                }
            ],
            "procedures": [
                {
                    "id": None,
                    "anatomic_location": None,
                    "code": "99213",
                    "code_type": "CPT",
                    "name": None,
                    "principal_procedure": None,
                    "quantity": None,
                    "rev_code": None,
                    "ordering_provider_id": "CSC:5272567F-E840-455D-9C09-CAB9602DC155",
                    "performing_provider_id": "CSC:334E678F-D256-4B9D-BFBF-224455D90684",
                    "results": None,
                    "status": None
                }
            ],
            "observations": [
                {
                    "id": None,
                    "code": "Tobacco use",
                    "name": "smoking status",
                    "value": "Tobacco User Temporarily Unknown",
                    "unit": "No unit"
                }
            ],
            "questionnaires": [],
            "results": []
        }
    ],
    "demographics": [
        {
            "patient_id": "4dbe5c7d-a03c-3a44-9245-7233fa0dcba5",
            "recorded": "2017-08-28T11:07:17.719Z",
            "sex": "Male"
        }
    ]
}


class TestCohortPatientsListView(TestCase):

    def setUp(self):
        admin = CurationUser.objects.get(
            email='mohan.jagabatthula@ggktech.com')
        self.client = APIClient()
        self.client.force_authenticate(user=admin)

        cohort1 = Cohort.objects.create(name='Rheumatoid Arthritis', description='Rheumatoid Arthritis patients')
        self.cohort1 = cohort1
        patient1 = Patient.objects.create(
            patient_id='4dbe5c7d-a03c-3a44-9245-7233fa0dcba5', deceased='yes', race='MC', sex_at_birth='male',
            date_of_birth='12th june', dob_is_year=True, cohort=cohort1
        )
        self.patient1 = patient1

        patient2 = Patient.objects.create(
            patient_id='9dbe4c3d-a03c-3a11-9245-1587fa0dcba5', deceased='yes', race='MC',
            sex_at_birth='male', date_of_birth='12th june', dob_is_year=True, cohort=cohort1
        )
        self.patient2 = patient2

        self.invalid_patient_input = {
            'patient_id': 'Patient3',
            'deceased': 'yes',
            'race': 'MC',
            'sex_at_birth': 'male',
            'date_of_birth': '12th june',
            'dob_is_year': True
        }

        self.valid_patient_input = valid_patient_input1

    def test_get_all_patients_in_domain(self):
        url = '/clinical/domains/{domain_id}/patients/'.format(
            domain_id=self.cohort1.id
        )
        response = self.client.get(url)
        patients = Patient.objects.all()
        serializer = PatientListSerializer(patients, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_an_invalid_patient_in_a_domain(self):
        url = '/clinical/domains/{domain_id}/patients/'.format(
            domain_id=self.cohort1.id
        )
        response = self.client.post(
            url, data=self.invalid_patient_input, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # def test_post_a_valid_patient_in_a_domain(self):
    #     url = '/clinical/domains/{domain_id}/patients/'.format(
    #         domain_id=self.cohort1.id
    #     )
    #     response = self.client.post(
    #         url, data=self.valid_patient_input, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCohortPatientsDetailView(TestCase):
    def setUp(self):
        admin = CurationUser.objects.get(
            email='mohan.jagabatthula@ggktech.com')
        self.client = APIClient()
        self.client.force_authenticate(user=admin)

        cohort1 = Cohort.objects.create(name='Rheumatoid Arthritis', description='Rheumatoid Arthritis patients')
        self.cohort1 = cohort1
        patient1 = Patient.objects.create(
            patient_id='4dbe5c7d-a03c-3a44-9245-7233fa0dcba5', deceased='yes', race='MC', sex_at_birth='male',
            date_of_birth='12th june', dob_is_year=True, cohort=cohort1
        )
        self.patient1 = patient1

        patient2 = Patient.objects.create(
            patient_id='9dbe4c3d-a03c-3a11-9245-1587fa0dcba5', deceased='yes', race='MC', sex_at_birth='male',
            date_of_birth='12th june', dob_is_year=True, cohort=cohort1
        )
        self.patient2 = patient2

        self.valid_patient_update = valid_patient_input1

    def test_get_patient_by_id(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_update_a_patient(self):
    #     url = '/clinical/domains/{domain_id}/patients/{patient_id}/'.format(
    #         domain_id=self.cohort1.id,
    #         patient_id=self.patient1.id
    #     )
    #     get_patient_response = self.client.get(url)
    #     patient_details = get_patient_response.data
    #     response = self.client.put(
    #         url, data=patient_details, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_a_patient(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
