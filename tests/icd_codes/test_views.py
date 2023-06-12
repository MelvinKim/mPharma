from django.test import TestCase
from django.urls import reverse
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from io import StringIO

from icd_codes.models import Diagnosis
from icd_codes.serializers import DiagnosisSerializer


class TestDiagnosisViews(APITestCase):
    def setUp(self):
        self.diagnosis = baker.make(Diagnosis)
        self.list_create_url = reverse('diagnosis-list-create')
        self.retrieve_update_delete_url = reverse(
            'diagnosis-retrieve-update-delete', args=[self.diagnosis.id])

    def test_get_diagnosis_list(self):
        response = self.client.get(self.list_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_diagnosis(self):
        data = {
            'category': 'A00',
            'block': '0',
            'subcategory': 'A000',
            'shortDescription': 'Sample short description',
            'longDescription': 'Sample long description',
            'icd_revision': '10'
        }
        response = self.client.post(self.list_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Diagnosis.objects.count(), 2)

    def test_retrieve_diagnosis(self):
        response = self.client.get(self.retrieve_update_delete_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.data, DiagnosisSerializer(self.diagnosis).data)

    def test_update_diagnosis(self):
        data = {
            'category': 'A00',
            'block': '0',
            'subcategory': 'A000',
            'shortDescription': 'Sample short description',
            'longDescription': 'Sample long description',
            'icd_revision': '10'
        }
        response = self.client.put(self.retrieve_update_delete_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_diagnosis = Diagnosis.objects.get(id=self.diagnosis.id)
        self.assertEqual(updated_diagnosis.category, 'A00')

    def test_delete_diagnosis(self):
        response = self.client.delete(self.retrieve_update_delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Diagnosis.objects.count(), 0)


class TestUploadCSVView(TestCase):
    def setUp(self):
        self.client = APIClient
        self.url = "/upload-csv/"

    def test_upload_csv(self):
        csv_data = StringIO(
            'code,name\nA00.0,Cholera due to Vibrio cholerae 01, biovar cholerae\n')
        response = self.client.post(
            self.url, {'csv_file': csv_data}, format='multipart')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
