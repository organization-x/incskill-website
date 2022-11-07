#IncSkill URL Configuration

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
    QuizOneView,
    #CodingExcerciseView, 
    )
import incskill_site.views as views

#urls are always accessed from top to bottom. to improve speeds, order the urls in highest to lowest priority/frequency
urlpatterns = [
    path('', LoginView.as_view(), name = 'login'),
    path('dashboard/', CoursePageView.as_view(), name = 'courses'),
    path('signup/', SignUpView.as_view(), name = "signup"),
    path('dashboard/course-one/', CourseOneView.as_view(), name = 'course_one'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('admin/', admin.site.urls),

    path('dashboard/course-one/resource-one', ResourceOneView.as_view(), name = 'resourceone'),
    path('dashboard/course-one/resource-two', ResourceTwoView.as_view(), name = 'resourcetwo'),
    path('dashboard/course-one/resource-three', ResourceThreeView.as_view(), name = 'resourcethree'),
    path('dashboard/course-one/resource-four', ResourceFourView.as_view(), name = 'resourcefour'),
    path('dashboard/course-one/resource-five', ResourceFiveView.as_view(), name = 'resourcefive'),
    path('dashboard/course-one/resource-six', ResourceSixView.as_view(), name = 'resourcesix'),
    path('dashboard/course-one/resource-seven', ResourceSevenView.as_view(), name = 'resourceseven'),
    path('dashboard/course-one/resource-eight', ResourceEightView.as_view(), name = 'resourceeight'),
    path('dashboard/course-one/resource-nine', ResourceNineView.as_view(), name = 'resourcenine'),
    path('dashboard/course-one/resource-ten', ResourceTenView.as_view(), name = 'resourceten'),
    path('dashboard/course-one/resource-eleven', ResourceElevenView.as_view(), name = 'resourceeleven'),
    path('dashboard/course-one/resource-twelve', ResourceTwelveView.as_view(), name = 'resourcetwelve'),

    path('dashboard/course-one/quiz-one', QuizOneView.as_view(), name = 'quizone'),
    path('dashboard/course-one/quiz-one/update-score/', views.score_updater , name="score_updater"),
    #the in-site code complier was temporarily removed due to numerous bugs
    #path('courses/course-one/coding-excercise', CodingExcerciseView.as_view(), name = 'codingexcercise')
]

handler404 = 'incskill_site.views.error_404_view'