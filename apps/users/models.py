
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    class Roles(models.TextChoices):
        SUPERADMIN = 'SUPERADMIN', 'Super Admin'
        ADMIN = 'ADMIN', 'Admin'
        USER = 'USER', 'User'
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.USER)
    branch = models.ForeignKey('branches.Branch', models.SET_NULL, null=True, blank=True)
    position = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    full_name = models.CharField(max_length=255, blank=True)
    objects = UserManager()
    def save(self, *args, **kwargs):
        if self.role == self.Roles.SUPERADMIN:
            self.is_superuser = self.is_staff = True
        elif self.role == self.Roles.ADMIN:
            self.is_superuser = False
            self.is_staff = True     # ← важно
        else:
            self.is_superuser = self.is_staff = False
        super().save(*args, **kwargs)


    def __str__(self):
        return self.username
