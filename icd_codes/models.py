from django.db import models

ICD_REVISIONS = (
    ('9', 'WHO ICD-9 Standard'),
    ('10', 'WHO ICD-10 Standard'),
    ('11', 'WHO ICD-11 Standard'),
)

# Diagnosis model
class Diagnosis(models.Model): 
    """
    A model for ICD-10 codes
    """
    category = models.CharField(max_length=12, blank=False, default="A00")
    block = models.CharField(max_length=12, default="0")
    subcategory = models.CharField(max_length=12, default="A000")
    shortDescription = models.TextField(default="short description sample")
    longDescription = models.TextField(default="long description sample")
    icd_revision = models.CharField(max_length=255, choices=ICD_REVISIONS)
    
    def __str__(self):
        return self.category