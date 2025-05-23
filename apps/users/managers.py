from django.contrib.auth.models import UserManager as DjangoUserManager

class UserManager(DjangoUserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('role', 'SUPERADMIN')   # ← добавляем роль
        return super().create_superuser(username, email, password, **extra_fields)
