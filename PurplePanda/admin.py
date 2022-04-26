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
        x = list(User.objects.all())
        return render(request, "viewdata.html", {'print':x})

    def post(self, request):
        return render(request, "viewdata.html", {})


class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html", {})

    def post(self, request):
        n = request.POST.get('name')
        p = request.POST.get('password')
        r = request.POST.get('role')
        if n != '' or p != '' or r != '':
            newUser = User(name=n, password=p, role=r)
            newUser.save()
        return redirect("/users/")


