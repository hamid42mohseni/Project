import random
from icecream import ic
from django.db import models
from django.contrib.auth.models import PermissionsMixin , AbstractBaseUser
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager
# # Manager For User
class Manager(BaseUserManager):
    def _create_user(self, username,password , phone_number, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username,phone_number = phone_number , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None , phone_number = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, password,phone_number, **extra_fields)

    def create_superuser(self, username, password, phone_number,  **extra_fields):
        if User.objects.filter(phone_number = phone_number).exists():
            raise('User PhoneNumber Already Exist')
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        # ic(username , password , phone_number)
        return self._create_user(username, password,phone_number, **extra_fields)
# #     # Use in Migrations
# #     use_in_migrations = True
# #     # Create User
# #     def create_user(self , phone_number):

# #         RandomPass = self.make_random_password(phone_number)
# #         # New Name For User Create
# #         CreateNameForUser =random.choice("abcdefghijkl") +  phone_number[-7:]
# #         while User.objects.filter(username = CreateNameForUser).exists():
# #              CreateNameForUser = random.choice("abcdefghijkl") +  phone_number[-7:]
# #         return self._create_user(username= CreateNameForUser  , password= RandomPass , phone_number= phone_number)
# #         # Create User
#     def _create_user(self , username , password , phone_number , is_active = True, is_staff = False , is_superuser = False , **extra_field):
#             TimeNow = timezone.now()
# #             # User Created
#             InserUser = self.model(username = username , phone_number = phone_number ,
#                                     date_joined = TimeNow,
#                                     is_superuser = is_superuser, 
#                                     is_staff = is_staff,
#                                     is_active = is_active,
#                                     password = password, **extra_field)            
#             InserUser.save(using = self.db)
#             return InserUser
# #     # Super User
#     def create_superuser(self,username, password):
#          return self._create_user(username= username , password=password , is_staff= True , is_superuser=True)

         
# # Create Table User
class User(AbstractBaseUser , PermissionsMixin):
    username = models.CharField(max_length=32 ,  unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15 , unique=True)
    is_active = models.BooleanField(default= True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default= timezone.now)    
    last_seen = models.DateTimeField(null=True , blank=True)
    objects = Manager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ['phone_number']
    class Meta :
        db_table = "Users"




