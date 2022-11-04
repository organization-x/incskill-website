from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    progress = models.IntegerField(default= 0)
    resource1 = models.BooleanField(default=False)
    resource2 = models.BooleanField(default=False)
    resource3 = models.BooleanField(default=False)
    resource4 = models.BooleanField(default=False)
    resource5 = models.BooleanField(default=False)
    resource6 = models.BooleanField(default=False)
    resource7 = models.BooleanField(default=False)
    resource8 = models.BooleanField(default=False)
    resource9 = models.BooleanField(default=False)
    resource10 = models.BooleanField(default=False)
    resource11 = models.BooleanField(default=False)
    resource12 = models.BooleanField(default=False)
    quiz = models.BooleanField(default = False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

@receiver(post_save, sender=User)
def calculate_progress(sender, instance, **kwargs):
    progress = instance.profile.progress = 0.0
    if instance.profile.resource1:
        progress += (100/14)
    if instance.profile.resource2:
        progress += (100/14)   
    if instance.profile.resource3:
        progress += (100/14)
    if instance.profile.resource4:
        progress += (100/14)
    if instance.profile.resource5:
        progress += (100/14)
    if instance.profile.resource6:
        progress += (100/14)
    if instance.profile.resource7:
        progress += (100/14) 
    if instance.profile.resource8:
        progress += (100/14)
    if instance.profile.resource9:
        progress += (100/14)
    if instance.profile.resource10:
        progress += (100/14)   
    if instance.profile.resource11:
        progress += (100/14)
    if instance.profile.resource12:
        progress += (100/14)
    if instance.profile.quiz:
        progress += (200/14)

    
    instance.profile.progress = int(round(progress))
    save_user_profile(sender=User, instance=instance)