from django.contrib import admin
from .models import Profile

# Registered the profile model to be accessible in the admin site

admin.site.register(Profile)