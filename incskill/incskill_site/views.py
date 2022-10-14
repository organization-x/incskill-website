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
        if 'resourcefour' in request.POST:
            return redirect('resourcefour')
        if 'resourcefive' in request.POST:
            return redirect('resourcefive')
        if 'resourcesix' in request.POST:
            return redirect('resourcesix')
        if 'resourceseven' in request.POST:
            return redirect('resourceseven')
        if 'resourceeight' in request.POST:
            return redirect('resourceeight')
        if 'resourcenine' in request.POST:
            return redirect('resourcenine')
        if 'resourceten' in request.POST:
            return redirect('resourceten')
        if 'resourceeleven' in request.POST:
            return redirect('resourceeleven')
        if 'resourcetwelve' in request.POST:
            return redirect('resourcetwelve')


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


class ResourceFourView(View):
    template_name = 'resource4.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceFiveView(View):
    template_name = 'resource5.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceSixView(View):
    template_name = 'resource6.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceSevenView(View):
    template_name = 'resource7.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceEightView(View):
    template_name = 'resource8.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceNineView(View):
    template_name = 'resource9.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceTenView(View):
    template_name = 'resource10.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceElevenView(View):
    template_name = 'resource11.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')


class ResourceTwelveView(View):
    template_name = 'resource12.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')