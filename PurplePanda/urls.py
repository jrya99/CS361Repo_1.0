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
from django.urls import path, include
from PurplePanda.login import Login, Home, Courses
from PurplePanda.admin import DataView, CreateUser, ViewCourses, CreateCourse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login.as_view()),
    path('home/', Home.as_view()),
    path('home/login.html', Login.as_view()),
    path('home/home.html', Home.as_view()),
    path('home/courses.html', Courses.as_view()),
    path('home/viewdata.html/', DataView.as_view()),
    path('home/viewdata.html/createuser.html', CreateUser.as_view()),
    path('home/viewcourse.html', ViewCourses.as_view()),
    path('home/viewcourse.html/createcourse.html', CreateCourse.as_view())
]
