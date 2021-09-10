from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True, primary_key=True)
    email = models.CharField(max_length=30, unique=True)
    kvk = models.CharField(max_length=30, unique=True,null=True)
    Telefoon =  models.CharField(max_length=30, unique=True,null=True)
    Adres = models.CharField(max_length=30, unique=True,null=True)
    Huisnummer = models.CharField(max_length=30, unique=True,null=True)
    Postcode = models.CharField(max_length=30, unique=True,null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
