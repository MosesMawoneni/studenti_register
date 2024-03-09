from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .managers import AccountsManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField("Your email", unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AccountsManager()

    def __str__(self):
        return self.email


class Student(models.Model):
    MALE_CHOICE = "MALE"
    FEMALE_CHOICE = "FEMALE"
    GENDER_CHOICES = [(MALE_CHOICE, "Male"), (FEMALE_CHOICE, "Female")]

    student = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    location = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    date_enrolled = models.DateField()
    name_of_guardian = models.CharField(max_length=255)
    is_prefect = models.BooleanField(default=False)
    gender = models.CharField(choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.student)


class Tutor(models.Model):
    MALE_CHOICE = "MALE"
    FEMALE_CHOICE = "FEMALE"
    GENDER_CHOICES = [(MALE_CHOICE, "Male"), (FEMALE_CHOICE, "Female")]

    SINGLE_CHOICE = "SINGLE"
    MARRIED_CHOICE = "MARRIED"
    MARITAL_STATUS_CHOICES = [(SINGLE_CHOICE, "Single"), (MARRIED_CHOICE, "Married")]

    tutor = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    location = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField()
    date_engaged = models.DateField()
    name_of_spouse = models.CharField(max_length=255, blank=True, null=True)
    marital_status = models.CharField(max_length=255, choices=MARITAL_STATUS_CHOICES)
    gender = models.CharField(choices=GENDER_CHOICES)

    def __str__(self):
        return str(self.tutor)
