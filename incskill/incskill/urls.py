"""incskill URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from incskill_site.views import (
    LoginView,
    CoursePageView,
    SignUpView,
    ProfileView,
    CourseOneView,
    ResourceOneView,
    ResourceTwoView,
    ResourceThreeView,
    ResourceFourView,
    ResourceFiveView,
    ResourceSixView,
    ResourceSevenView,
    ResourceEightView,
    ResourceNineView,
    ResourceTenView,
    ResourceElevenView,
    ResourceTwelveView,
    QuizOneView    
    )


urlpatterns = [
    path('', LoginView.as_view(), name = 'login'),
    path('courses/', CoursePageView.as_view(), name = 'courses'),
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('courses/course-one/', CourseOneView.as_view(), name = 'course_one'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('admin/', admin.site.urls),
    path('courses/course-one/resource-one', ResourceOneView.as_view(), name = 'resourceone'),
    path('courses/course-one/resource-two', ResourceTwoView.as_view(), name = 'resourcetwo'),
    path('courses/course-one/resource-three', ResourceThreeView.as_view(), name = 'resourcethree'),
    path('courses/course-one/resource-four', ResourceFourView.as_view(), name = 'resourcefour'),
    path('courses/course-one/resource-five', ResourceFiveView.as_view(), name = 'resourcefive'),
    path('courses/course-one/resource-six', ResourceSixView.as_view(), name = 'resourcesix'),
    path('courses/course-one/resource-seven', ResourceSevenView.as_view(), name = 'resourceseven'),
    path('courses/course-one/resource-eight', ResourceEightView.as_view(), name = 'resourceeight'),
    path('courses/course-one/resource-nine', ResourceNineView.as_view(), name = 'resourcenine'),
    path('courses/course-one/resource-ten', ResourceTenView.as_view(), name = 'resourceten'),
    path('courses/course-one/resource-eleven', ResourceElevenView.as_view(), name = 'resourceeleven'),
    path('courses/course-one/resource-twelve', ResourceTwelveView.as_view(), name = 'resourcetwelve'),
    path('courses/course-one/quiz-one', QuizOneView.as_view(), name = 'quizone')
]