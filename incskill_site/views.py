from django.shortcuts import HttpResponse
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
    error_message = "Information is Incorrect!"
    notvalid = False
    def get(self, request):
        if not request.user.is_authenticated:
            context = {
                "input_notvalid" : SignUpView.notvalid,
                "error_message" : SignUpView.error_message, 
            }
            return render(request, self.template_name, context)
        else:
            return redirect('courses')

    def post(self, request):
        if 'submit' in request.POST:
            SignUpView.notvalid=False
            get_mail = request.POST['email']
            get_name = request.POST['username']
            get_pass = request.POST['password']
            if get_mail == None or get_mail == '':
                print("No email entered!")
                SignUpView.notvalid=True
                SignUpView.error_message = "No email entered!"
                return render(request, self.template_name, {"input_notvalid" : SignUpView.notvalid, "error_message" : SignUpView.error_message})
            if get_name == None or get_name == '':
                print("No username entered!")
                SignUpView.notvalid=True
                SignUpView.error_message = "No username entered!"
                return render(request, self.template_name, {"input_notvalid" : SignUpView.notvalid, "error_message" : SignUpView.error_message})
            else:
                print("Username: " + get_name)
            if get_pass == None or get_pass == '':
                print("No password entered!")
                SignUpView.notvalid=True
                SignUpView.error_message = "No password entered!"
                return render(request, self.template_name, {"input_notvalid" : SignUpView.notvalid, "error_message" : SignUpView.error_message})
            
            print('forms filled')
            if User.objects.filter(email=get_mail).exists():
                print("Email is not unique")
                SignUpView.notvalid=True
                SignUpView.error_message = "Email is not unique!"
                return render(request, self.template_name, {"input_notvalid" : SignUpView.notvalid, "error_message" : SignUpView.error_message})
            if User.objects.filter(username=get_name).exists():
                print("Username is not unique")
                SignUpView.notvalid=True
                SignUpView.error_message = "Username is not unique!"
                return render(request, self.template_name, {"input_notvalid" : SignUpView.notvalid, "error_message" : SignUpView.error_message})
            user = User.objects.create_user(email = get_mail, username = get_name, password = get_pass)
            print('user created')
            return redirect("login")


        if 'login' in request.POST:
            SignUpView.notvalid=False
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
    gotodiv = ''
    def get(self, request):
        print("Something")
        ResourceOneView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceOneView.gotodiv})
        else:
            return redirect('login')
    
    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource1 == False):
                request.user.profile.resource1 = True        
            else: 
                request.user.profile.resource1 = False
            ResourceOneView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceOneView.gotodiv})

class ResourceTwoView(View):
    template_name = 'resource2.html'
    gotodiv = ''
    def get(self, request):
        ResourceTwoView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceTwoView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        gotodiv = ''
        if 'submit' in request.POST:
            if (request.user.profile.resource2 == False):
                request.user.profile.resource2 = True
            else: 
                request.user.profile.resource2 = False
            ResourceTwoView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceTwoView.gotodiv})


class ResourceThreeView(View):
    template_name = 'resource3.html'
    gotodiv = ''
    def get(self, request):
        ResourceThreeView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceThreeView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource3 == False):
                request.user.profile.resource3= True
            else: 
                request.user.profile.resource3= False
            ResourceThreeView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceThreeView.gotodiv})

class ResourceFourView(View):
    template_name = 'resource4.html'
    gotodiv = ''
    def get(self, request):
        ResourceFourView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceFourView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource4 == False):
                request.user.profile.resource4 = True
            else: 
                request.user.profile.resource4 = False
            ResourceFourView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceFourView.gotodiv})


class ResourceFiveView(View):
    template_name = 'resource5.html'
    gotodiv = ''
    def get(self, request):
        ResourceFiveView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceFiveView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource5 == False):
                request.user.profile.resource5 = True
            else: 
                request.user.profile.resource5 = False
            ResourceFiveView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceFiveView.gotodiv})

class ResourceSixView(View):
    template_name = 'resource6.html'
    gotodiv = ''
    def get(self, request):
        ResourceSixView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceSixView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource6 == False):
                request.user.profile.resource6 = True
            else: 
                request.user.profile.resource6 = False
            ResourceSixView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceSixView.gotodiv})


class ResourceSevenView(View):
    template_name = 'resource7.html'
    gotodiv = ''
    def get(self, request):
        ResourceSevenView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceSevenView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource7 == False):
                request.user.profile.resource7 = True
            else: 
                request.user.profile.resource7 = False
            ResourceSevenView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceSevenView.gotodiv})

class ResourceEightView(View):
    template_name = 'resource8.html'
    gotodiv = ''
    def get(self, request):
        ResourceEightView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceEightView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource8 == False):
                request.user.profile.resource8 = True
            else: 
                request.user.profile.resource8 = False
            ResourceEightView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceEightView.gotodiv})

class ResourceNineView(View):
    template_name = 'resource9.html'
    gotodiv = ''
    def get(self, request):
        ResourceNineView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceNineView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource9 == False):
                request.user.profile.resource9 = True
            else: 
                request.user.profile.resource9 = False
            ResourceNineView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceNineView.gotodiv})


class ResourceTenView(View):
    template_name = 'resource10.html'
    gotodiv = ''
    def get(self, request):
        ResourceTenView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceTenView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource10 == False):
                request.user.profile.resource10= True
            else: 
                request.user.profile.resource10 = False
            ResourceTenView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceTenView.gotodiv})


class ResourceElevenView(View):
    template_name = 'resource11.html'
    gotodiv = ''
    def get(self, request):
        ResourceElevenView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceElevenView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource11 == False):
                request.user.profile.resource11 = True
            else: 
                request.user.profile.resource11 = False
            ResourceElevenView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceElevenView.gotodiv})


class ResourceTwelveView(View):
    template_name = 'resource12.html'
    gotodiv = ''
    def get(self, request):
        ResourceTwelveView.gotodiv = '#'
        if request.user.is_authenticated:
            return render(request, self.template_name, {'div': ResourceTwelveView.gotodiv})
        else:
            return redirect('login')

    def post(self, request):
        if 'submit' in request.POST:
            if (request.user.profile.resource12 == False):
                request.user.profile.resource12 = True
            else: 
                request.user.profile.resource12 = False
            ResourceTwelveView.gotodiv = 'btnset'
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name, {'div': ResourceTwelveView.gotodiv})


def score_updater(request):
    print("score_update requested")
    print(request.POST)
    if request.method == 'POST':
        if 'playerScore' in request.POST:
            QuizOneView.playerScore = request.POST['playerScore']
            return HttpResponse('success')
    return HttpResponse('fail')

class QuizOneView(View):
    template_name = 'quiz1.html'
    playerScore = 0
    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name)
        else:
            return redirect('login')

    def post(self, request):
 #       if 'submit' in request.POST:
 #           if (request.user.profile.quiz1 == False):
 #               request.user.profile.quiz1 = True
 #           else: 
 #               request.user.profile.quiz1 = False
            print("submitted")
            print("Score: " + str(QuizOneView.playerScore))
            if int(QuizOneView.playerScore) >= 7: 
                request.user.profile.quiz = True
            else:
                request.user.profile.quiz = False
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
        print ("Post: " + request.POST)
        if 'submit' in request.POST:
            if (request.user.profile.quiz1 == False):
                request.user.profile.quiz1 = True
            else: 
                request.user.profile.quiz1 = False
            print("submitted")
            save_user_profile(sender=User, instance=request.user)
            return render(request, self.template_name)

def error_404_view(request, exception):
    return render(request, '404.html')