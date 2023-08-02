import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager, Group as BaseGroup
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from django.utils import timezone
from resources.verification import *
from statics.models import *


def user_photo_path(user, filename):
    return f'users/photos/{user}_{filename}'


def user_license_path(user, filename):
    return f'users/license/{user}_{filename}'


class UserManager(BaseUserManager):
    def create_user(self, **data):
        password = data.pop('password')
        if data.get('role') == User.ROLE_PATIENT:
            data['accepted'] = True
        user = self.create(**data)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        return self.create_user(email=email, password=password, is_staff=True, is_superuser=True)
        
    
class User(AbstractUser):
    objects = UserManager()

    def send_verification_code_email_message(self):
        code = get_verification_code()
        self.email_code = make_password(code)
        self.email_code_time = timezone.now()
        self.save()
        send_verification_code_email_message(code, self.email)

    def change_email(self, email):
        self.email = email
        self.email_code = None
        self.email_code_time = None
        self.email_verified = False
        self.save()

    def verify_email(self):
        self.email_verified = True
        self.save()

    ROLE_DOCTOR = 0
    ROLE_PATIENT = 1

    ROLE_CHOICES = (
        (ROLE_DOCTOR, 'Doctor'), 
        (ROLE_PATIENT, 'Patient'),
    )
    
    username=models.CharField(max_length=100, unique=False, null=True, blank=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    email = models.CharField(max_length=255, unique=True)
    email_code = models.CharField(max_length=500, null=True, blank=True)
    email_code_time = models.DateTimeField(null=True, blank=True)
    email_verified = models.BooleanField(default=False)

    role = models.PositiveIntegerField(choices=ROLE_CHOICES, null=True, blank=True)
    accepted = models.BooleanField(default=False)

    # ------------------------------------------------------------------------------------

    GENDER_MALE = 0
    GENDER_FEMALE = 1

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )
    
    BLOOD_TYPE_O_POSITIVE = 0
    BLOOD_TYPE_A_POSITIVE = 1
    BLOOD_TYPE_B_POSITIVE = 2
    BLOOD_TYPE_AB_POSITIVE = 3
    BLOOD_TYPE_O_NEGATIVE = 4
    BLOOD_TYPE_A_NEGATIVE = 5
    BLOOD_TYPE_B_NEGATIVE = 6
    BLOOD_TYPE_AB_NEGATIVE = 7

    BLOOD_TYPE_CHOICES = (
        (BLOOD_TYPE_O_POSITIVE, 'O+'),
        (BLOOD_TYPE_A_POSITIVE, 'A+'),
        (BLOOD_TYPE_B_POSITIVE, 'B+'),
        (BLOOD_TYPE_AB_POSITIVE, 'AB+'),
        (BLOOD_TYPE_O_NEGATIVE, 'O-'),
        (BLOOD_TYPE_A_NEGATIVE, 'A-'),
        (BLOOD_TYPE_B_NEGATIVE, 'B-'),
        (BLOOD_TYPE_AB_NEGATIVE, 'AB-'),
    )

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=50, unique=False, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES, null=True, blank=True)
    photo = models.ImageField(max_length=500, upload_to=user_photo_path, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.PROTECT, null=True, blank=True)
    
    blood_type = models.IntegerField(choices=BLOOD_TYPE_CHOICES, null=True, blank=True)
    length = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    chronic_disease = models.TextField(null=True, blank=True)
    genetic_disease = models.TextField(null=True, blank=True)
    other_info = models.TextField(null=True, blank=True)
    
    license = models.ImageField(max_length=500, upload_to=user_photo_path, null=True, blank=True)
    available_for_meeting = models.BooleanField(default=False)
    specialization = models.ForeignKey(Specialization, on_delete=models.PROTECT, null=True, blank=True)

    REQUIRED_FIELDS = ['password']
    USERNAME_FIELD ='email'

    def __str__(self) -> str:
        return f'{self.id} - {self.email}'
    

class Group(BaseGroup):
    class Meta:
        proxy = True

