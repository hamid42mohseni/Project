from django.db import models
from django.contrib.auth.models import PermissionsMixin , AbstractBaseUser
from django.utils import timezone
from .manager import Manager
# Create Table User
class Acounts(AbstractBaseUser , PermissionsMixin):

    username = models.CharField(max_length=32 , null=True , blank=True)
    phone_number = models.CharField(max_length=13 , unique=True)

    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default= timezone.now)    
    last_seen = models.DateTimeField(null=True)


    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['username']
    class Meta :
        db_table = "Acounts"
