from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from incskill_site.models import Profile, create_user_profile, save_user_profile, calculate_progress


class var:
    notvalid = False


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
#                user.profile.progress = .3
                return redirect('courses')
            else:
                return render(request, self.template_name)
        if 'signup' in request.POST:
            return redirect('signup')

            
class CoursePageView(View):
    template_name = 'coursePage.html'
    def get(self, request):
        if request.user.is_authenticated:
            calculate_progress(sender=User, instance=request.user)
            return render(request, self.template_name)
        else:
            return redirect('login')


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
        var.notvalid=False
        if 'submit' in request.POST:
            try:
                get_mail = request.POST['email']
                get_name = request.POST['username']
                get_pass = request.POST['password']
                if get_mail != None and get_mail != '':
                    if get_name != None and get_name != '':
                        print("Username: " + get_name)
                        if get_pass != None and get_pass != '':
                            var.notvalid=False
                            print('forms filled')
                            user = User.objects.create_user(email = get_mail, username = get_name, password = get_pass)
                            print('user created')
                            return redirect('login')
                        else:
                            print('empty pass')
                    else:
                        print('empty name')
                else:
                    print('empty mail')

                var.notvalid=True
                print('forms blank')
                return redirect('signup')
            except IntegrityError:
                var.notvalid=True
                print('integrity error')
                return redirect('signup')
            except ValueError:
                var.notvalid=True
                print('value error')
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
            calculate_progress(sender=User, instance=request.user)
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
        if 'quizone' in request.POST:
            return redirect('quizone')
        if 'codingexcercise' in request.POST:
            return redirect('codingexcercise')


class ResourceOneView(View):
    template_name = 'resource1.html'
    def get(self, request):
        print("Something")
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')
    
    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource1 == False):
                request.user.profile.resource1 = True
            else: 
                request.user.profile.resource1 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)


class ResourceTwoView(View):
    template_name = 'resource2.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource2 == False):
                request.user.profile.resource2 = True
            else: 
                request.user.profile.resource2 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)


class ResourceThreeView(View):
    template_name = 'resource3.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource3 == False):
                request.user.profile.resource3= True
            else: 
                request.user.profile.resource3= False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceFourView(View):
    template_name = 'resource4.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource4 == False):
                request.user.profile.resource4 = True
            else: 
                request.user.profile.resource4 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceFiveView(View):
    template_name = 'resource5.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource5 == False):
                request.user.profile.resource5 = True
            else: 
                request.user.profile.resource5 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceSixView(View):
    template_name = 'resource6.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource6 == False):
                request.user.profile.resource6 = True
            else: 
                request.user.profile.resource6 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceSevenView(View):
    template_name = 'resource7.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource7 == False):
                request.user.profile.resource7 = True
            else: 
                request.user.profile.resource7 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceEightView(View):
    template_name = 'resource8.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource8 == False):
                request.user.profile.resource8 = True
            else: 
                request.user.profile.resource8 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceNineView(View):
    template_name = 'resource9.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource9 == False):
                request.user.profile.resource9 = True
            else: 
                request.user.profile.resource9 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceTenView(View):
    template_name = 'resource10.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource10 == False):
                request.user.profile.resource10= True
            else: 
                request.user.profile.resource10 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceElevenView(View):
    template_name = 'resource11.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource11 == False):
                request.user.profile.resource11 = True
            else: 
                request.user.profile.resource11 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class ResourceTwelveView(View):
    template_name = 'resource12.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource12 == False):
                request.user.profile.resource12 = True
            else: 
                request.user.profile.resource12 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)


class QuizOneView(View):
    template_name = 'quiz1.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.quiz1 == False):
                request.user.profile.quiz1 = True
            else: 
                request.user.profile.quiz1 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

class CodingExcerciseView(View):
    template_name = 'exampleCode.html'
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.quiz1 == False):
                request.user.profile.quiz1 = True
            else: 
                request.user.profile.quiz1 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)