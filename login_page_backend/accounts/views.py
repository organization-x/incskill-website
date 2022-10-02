from http.client import HTTPResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("loginPage")
    template_name = "Register.html"

def home_view(request, *args, **kwargs):
    return HTTPResponse("loginPage.html")