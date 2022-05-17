"""PurplePanda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from PurplePanda.views import Login, Home, Courses, DataView, CreateUser, ViewCourses, CreateCourse, Profile, AssignInstructor, AssignTA, ViewMessage, SendMessage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view(), name='home'),
    path('viewuser/', DataView.as_view(), name='viewuser'),
    path('createuser/', CreateUser.as_view(), name='createuser'),
    path('viewcourse/', ViewCourses.as_view(), name='viewcoures'),
    path('createcourse/', CreateCourse.as_view(), name='createcourse'),
    path('profile/', Profile.as_view(), name='profile'),
    path('assigninstructor/', AssignInstructor.as_view(), name='assigninstructor'),
    path('assignta/', AssignTA.as_view(), name='assignta'),
    path('viewmessage/', ViewMessage.as_view(), name='viewmessage'),
    path('sendmessage/', SendMessage.as_view(), name='sendmessage')
]
