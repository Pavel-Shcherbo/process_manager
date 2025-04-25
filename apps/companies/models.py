
from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=64, blank=True)
    road = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
