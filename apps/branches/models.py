
from django.db import models

class Branch(models.Model):
    company = models.ForeignKey('companies.Company', models.CASCADE, related_name='branches')
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.company.short_name or self.company.name} / {self.name}'
