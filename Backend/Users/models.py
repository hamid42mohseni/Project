# from icecream import ic
from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager


# # Manager For User
class Manager(BaseUserManager):
    #   Use in Migrations
    use_in_migrations = True

    def _create_user(self, username, password, phone_number, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password, phone_number, **extra_fields):
        if User.objects.filter(phone_number=phone_number).exists():
            raise ("User PhoneNumber Already Exist")  # type: ignore
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self._create_user(username, password, phone_number, **extra_fields)


# # Create Table User
class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)
    phone_number = models.CharField(max_length=15, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_seen = models.DateTimeField(null=True, blank=True)
    objects = Manager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["phone_number"]

    class Meta:
        db_table = "Users"
