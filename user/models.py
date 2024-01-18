from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]