"""This module tests appointment API."""

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from ....users.models import CurationUser
from ...models.appointment import Appointment
from ...models.cohort import Cohort
from ...models.patient import Patient
from ...serializers.appointment import AppointmentSerializer


class TestAppointmentListView(TestCase):
    """
    Test appointment API endpoints
    """

    def setUp(self):
        admin = CurationUser.objects.get(email='mohan.jagabatthula@ggktech.com')
        self.client = APIClient()
        self.client.force_authenticate(user=admin)
        cohort1 = Cohort.objects.create(name='karthik', description='Engineer')
        self.cohort1 = cohort1

        patient1 = Patient.objects.create(
            patient_id='4dbe5c7d-a03c-3a44-9245-7233fa0dcba5',
            deceased="No deceased indicator present", race='White',
            sex_at_birth='Female', date_of_birth='1958',
            dob_is_year=True, cohort=cohort1
        )
        self.patient1 = patient1
        appointments = []
        appointments.append(Appointment(
            data_source_id='1', provider_id='1982732558',
            facility_id='CSC:9D458E61-2B5A-4504-9016-7FD123456EE2', start='2017-01-19 00:00:00', patient=patient1
        ))
        appointments.append(Appointment(
            data_source_id='2', provider_id='1982732558',
            facility_id='CSC:9D487E61-2B5A-4504-9016-7FD123457EE2', start='2017-02-19 00:00:00', patient=patient1
        ))
        appointments.append(Appointment(
            data_source_id='3', provider_id='1982732558',
            facility_id='CSC:9D896E61-2B5A-4504-9016-7FD123474EE2', start='2017-03-19 00:00:00', patient=patient1
        ))
        Appointment.objects.bulk_create(appointments)

        self.invalid_appointment_input = {
            'patient': 'patient_id',
            'user': {'email': 'nadeem.saif@ggktech.com'}
        }

        self.valid_appointment_input = {
            'data_source_id': '4',
            'provider_id': '1982732558',
            'facility_id': 'CSC:9D487E61-2B5A-4504-9016-7FD123457EE2',
            'start': '2017-02-29 00:00:00',
            'procedures_scheduled': []
        }

        self.app = Appointment.objects.create(
            data_source_id='5', provider_id='1982732558',
            facility_id='CSC:9D487E61-2B5A-4874-1598-7FD123457EE2',
            start='2017-12-29 00:00:00', patient=patient1
        )

        self.valid_appointment_update = {
            'data_source_id': '6',
            'provider_id': '1982732558',
            'facility_id': 'CSC:9D111E61-2B5A-4504-9016-7FD784557EE2',
            'start': '2017-07-09 00:00:00',
            'procedures_scheduled': []
        }

    def test_get_all_appointments(self):
        # get API response
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id
        )
        response = self.client.get(url)
        # get data from db
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        #self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_appointments(self):
        # get API response
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/?searchParam={searchParam}'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id,
            searchParam='DOESNOTEXIST'
        )
        response = self.client.get(url)
        # get data from db
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(0, response.data['count'])

    def test_post_a_valid_appointment(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id
        )
        response = self.client.post(url, data=self.valid_appointment_input, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_an_invalid_appointment(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id
        )
        response = self.client.post(url, data=self.invalid_appointment_input, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    # Testing AppointmentDetailsView class from here
    # def test_get_appointment_by_id(self):
    #     # testing get_appointment_with_id
    #     url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/{appointment_id}/'.format(
    #         domain_id=self.cohort1.id,
    #         patient_id=self.patient1.id,
    #         appointment_id=self.app.id
    #     )
    #     response = self.client.get(url)
    #     appointment = Appointment.objects.get(data_source_id='2')
    #     serializer = AppointmentSerializer(appointment)
    #     # self.assertEqual(response.data, serializer.data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_updating_an_appointment(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/{appointment_id}/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id,
            appointment_id=self.app.id
        )
        response = self.client.put(url, data=self.valid_appointment_update, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_an_appointment(self):
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/{appointment_id}/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id,
            appointment_id=self.app.id
        )
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_invalid_appointment_by_id(self):
        # testing get_appointment_with_id
        url = '/clinical/domains/{domain_id}/patients/{patient_id}/appointments/{appointment_id}/'.format(
            domain_id=self.cohort1.id,
            patient_id=self.patient1.id,
            appointment_id=123
        )
        response = self.client.get(url)
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
