from django.shortcuts import render, redirect
from django.views import View
from PurplePanda.models import User, Courses


class Login(View):
    def get(self, request):
        return render(request, "../static/../templates/login.html", {})

    def post(self, request):
        bad_password = False
        try:
            x = User.objects.get(name=request.POST['name'])
        except x.DoesNotExist:
            return render(request, "../static/../templates/login.html", {"message": "Error: User doesn't exist"})
        bad_password = (x.password != request.POST["password"])

        if bad_password:
            return render(request, "../static/../templates/login.html", {"message": "password is incorrect, please try again!"})
        else:
            request.session["name"] = x.name
            if x.role == "admin":
                return redirect("/home/")
            else:
                return redirect("/home/")


class Home(View):
    def get(self, request):
        return render(request, "../static/../templates/home.html", {})


class Courses(View):
    def get(self, request):
        x = request.session["name"]
        return render(request, "../static/../templates/courses.html", {})


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
        return redirect('/home/')


class ViewCourses(View):
    def get(self, request):
        x = list(Courses.objects.all())
        return render(request, "viewcourse.html", {"print": x})

    def post(self, request):
        return render(request, "viewcourse.html", {})


class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        n = request.POST.get('name')
        if n != '':
            newCourse = Courses(courseName=n)
            newCourse.save()
        return redirect('/home/')
