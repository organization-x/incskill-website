from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=40)
    is_staff = models.BooleanField()
    is_superuser = models.BooleanField()
    course_progress_one = models.DecimalField(default=0.0, editable = False, max_digits=3, decimal_places=2)
    #the idea is each completed section/quiz/excersize will contribute a percentage shown as a decimal to the user's progress. 100% completetion is 1.00

    def __str__(self):
        return self.name()

