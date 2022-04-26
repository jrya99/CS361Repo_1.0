from PurplePanda.parent import Parent
from django.views import View
from django.shortcuts import render, redirect
from PurplePanda.models import User


class Admin(Parent):

    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def create_class(self, class_id, class_name):
        pass


class DataView(View):
    def get(self, request):
        return render(request, "ViewData.html", {})

    def post(self, request):
        return render(request, "ViewData.html", {"print": User.objects.all()})


