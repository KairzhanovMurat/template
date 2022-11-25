from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class Account(AbstractUser):
    username = models.CharField(max_length=10, unique=False, default='')
    email = models.EmailField(("email address"), unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
