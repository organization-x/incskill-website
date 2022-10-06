from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('courses')
    
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


class CoursePageView(View):
    template_name = 'coursePage.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

#testing something out
#    def get(self, request):
#        if request.user.is_authenticated:
#           course_progress_one = request.GET['progress']
#           return render(course_progress_one, request, self.template_name)
#        else:
#            return redirect('login')
        
    def post(self, request):
        return redirect('course_one')
    

class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('courses')

    def post(self, request):
        if 'submit' in request.POST:
            userName = request.POST['username']
            userPass = request.POST['password']
            userMail = request.POST['email']
            user = User.objects.create_user(username = userName, email = userMail, password = userPass)
            return redirect('login')

        if 'login' in request.POST:
            return redirect('login')


class ProfileView(View):
    template_name = 'profile.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')
        
    def post(self, request):
        if 'logout' in request.POST:
            logout(request)
            return redirect('login')
        else:
            return render(request, self.template_name)


class CourseOneView(View):
    template_name = 'courseOne.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'resourceone' in request.POST:
            return redirect('resourceone')
        if 'resourcetwo' in request.POST:
            return redirect('resourcetwo')
        if 'resourcethree' in request.POST:
            return redirect('resourcethree')


class ResourceOneView(View):
    template_name = 'resource1.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceTwoView(View):
    template_name = 'resource2.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceThreeView(View):
    template_name = 'resource3.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')
