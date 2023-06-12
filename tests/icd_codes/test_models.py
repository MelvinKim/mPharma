from django.core.exceptions import ValidationError
from django.test import TestCase
from model_bakery import baker

from icd_codes.models import Diagnosis


class TestDiagnosisModel(TestCase):
    def test_diagnosis_creation(self):
        diagnosis = baker.make(
            Diagnosis,
            category='A00',
            block='0',
            subcategory='A000',
            shortDescription='Cholera',
            longDescription='Cholera due to Vibrio cholerae 01, biovar cholerae',
            icd_revision='10'
        )

        self.assertEqual(diagnosis.category, 'A00')
        self.assertEqual(diagnosis.block, '0')
        self.assertEqual(diagnosis.subcategory, 'A000')
        self.assertEqual(diagnosis.shortDescription, 'Cholera')
        self.assertEqual(diagnosis.longDescription,
                         'Cholera due to Vibrio cholerae 01, biovar cholerae')
        self.assertEqual(diagnosis.icd_revision, '10')
