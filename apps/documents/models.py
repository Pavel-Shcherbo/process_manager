
from django.db import models
from django.utils import timezone
import os

def document_upload_path(instance, filename):
    company = instance.process.branch.company
    return f'documents/{company.id}/{filename}'

class Document(models.Model):
    class DocTypes(models.TextChoices):
        POLICY = 'policy', 'Policy'
        INSTRUCTION = 'instruction', 'Instruction'
        REGULATION = 'regulation', 'Regulation'
        OTHER = 'other', 'Other'

    process = models.ForeignKey('processes.Process', models.CASCADE, related_name='documents')
    number = models.CharField(max_length=50)
    title = models.CharField(max_length=255)
    doc_type = models.CharField(max_length=20, choices=DocTypes.choices)
    signed_at = models.DateField(default=timezone.now)
    file = models.FileField(upload_to=document_upload_path)

    def filename(self):
        return os.path.basename(self.file.name)

    def __str__(self):
        return f'{self.number} - {self.title}'
