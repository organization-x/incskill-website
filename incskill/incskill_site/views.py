from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from cerberus import Validator


class var:
    notvalid = False
    mail_schema = {'name': {'type': 'string'}}
    val_mail = Validator(mail_schema)
    name_schema = {'name': {'type': 'string'}}
    val_name = Validator(name_schema)
    pass_schema = {'name': {'type': 'string'}}
    val_pass = Validator(pass_schema)



# Create your views here.	# Create your views here.
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
            context = {
                "input_notvalid" : var.notvalid,
            }
            return render(request, self.template_name, context)
        else:
            return redirect('courses')

    def post(self, request):
        if 'submit' in request.POST:
            get_mail = request.POST['email']
            user_mail = {'name' : get_mail }
            valid_mail = var.val_mail.validate(user_mail, var.mail_schema)

            get_name = request.POST['username']
            user_name = {'name' : get_name}
            valid_name = var.val_name.validate(user_name, var.name_schema)

            get_pass = request.POST['password']
            user_pass = {'name' : get_pass}
            valid_pass = var.val_pass.validate(user_pass, var.pass_schema)


            try:
                if valid_mail and valid_name and valid_pass:
                    var.notvalid=False
                    user = User.objects.create_user(email = get_mail, username = get_name, password = get_pass)
                    return redirect('login')
                else:
                    var.notvalid=True
                    return redirect('signup')
            except ValueError:
                var.notvalid=True
                return redirect('signup')

        if 'login' in request.POST:
            var.notvalid=False
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