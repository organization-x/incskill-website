from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=40)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()

    def __str__(self):
        return self.name()

