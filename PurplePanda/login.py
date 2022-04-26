from django.shortcuts import render, redirect
from django.views import View
from PurplePanda.models import User


class Login(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        bad_password = False

        x = User.objects.get(name=request.POST['name'])
        bad_password = (x.password != request.POST["password"])

        if bad_password:
            return render(request, "login.html", {"message": "password is incorrect, please try again!"})
        else:
            request.session["name"] = x.name
            if x.role == "admin":
                return redirect("/home/")
            else:
                return redirect("/home/")


class Home(View):
    def get(self, request):
        x = request.session["name"]
        return render(request, "home.html", {})
