# Stdlib Imports
from typing import List

# Django Imports
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

##### Local Imports #####
from authy.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=255, help_text="The user fullname.")
    email = models.EmailField(
        max_length=255,
        unique=True,
        help_text="The user email address.",
    )
    phone_number = models.CharField(
        max_length=11,
        help_text="The user phone number.",
        blank=True,
        null=True,
    )
    is_active = models.BooleanField(
        default=False,
        help_text="Is the user account active? Default is False.",
    )
    is_staff = models.BooleanField(
        default=False, help_text="Is the user a staff? Default is False."
    )
    password = models.CharField(
        max_length=128,
        validators=[
            MaxLengthValidator(limit_value=128),
        ],
    )
    date_created = models.DateTimeField(
        auto_now_add=True, help_text="The date and time user was created."
    )
    date_modified = models.DateTimeField(
        auto_now=True, help_text="The date and time user user modified."
    )
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS: List[str] = ["full_name", "phone_number"]

    class Meta:
        db_table = "users"
        verbose_name_plural = "Users"
        indexes = [models.Index(fields=["email", "phone_number"])]

    def __str__(self) -> str:
        return self.full_name


class Student(models.Model):
    """
    id: auto generated
    """

    student_number = models.CharField(max_length=10)
    student_name = models.CharField(max_length=100)
    faculty_name = models.CharField(max_length=100)
    student_email = models.CharField(max_length=256)
    date_of_birth = models.DateTimeField()
    
    def __str__(self) -> str:
        return self.student_name