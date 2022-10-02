from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login

# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        if 'submit' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('courses')
            else:
                return render(request, self.template_name)
        if 'signup' in request.POST:
            return redirect('signup')


class CoursePageView(TemplateView):
    template_name = 'coursePage.html'
    
class SignUpView(TemplateView):
    template_name = 'signup.html'