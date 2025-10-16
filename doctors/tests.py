from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from patients.models import Patient
from doctors.models import Doctor


class DoctorViewSetTests(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(
            first_name="John",
            last_name="Patient",
            date_of_birth="1990-01-01",
            contact_number="12345678",
            email="example@example.com",
            address="Calle X",
            medical_history="Ninguna",
        )
        self.doctor = Doctor.objects.create(
            first_name="John",
            last_name="Doctor",
            qualification="Profesional",
            contact_number="12345678",
            email="example2@example.com",
            address="Calle Y",
            biography="Ninguna",
            is_on_vacation=False,
        )
        self.client = APIClient()

    def test_list_should_return_200(self):
        url = reverse(
            "doctor-appointments",
            kwargs={"pk": self.doctor.id},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)