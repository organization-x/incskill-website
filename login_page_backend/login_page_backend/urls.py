from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='login.html'), name='login'),
    path('signup/', TemplateView.as_view(template_name='signup.html'), name='signup'),
    path('courses/', TemplateView.as_view(template_name='coursePage.html'), name='courses'),
    path('courses/one', TemplateView.as_view(template_name='courseOne.html'), name='cOne'),
    #path('courses/two', TemplateView.as_view(template_name='courseTwo.html'), name='cTwo'),
    #we might want to add more specific link names 
]

