from django.shortcuts import render, redirect
from django.views import View
from PurplePanda.models import MyUser, MyCourses
from django.shortcuts import HttpResponse


class Login(View):
    def get(self, request):
        return render(request, "../static/../templates/login.html", {})

    def post(self, request):
        print('hi')
        bad_password = False
        try:
            x = MyUser.objects.get(name=request.POST['name'])
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
        print('hi4')
        x = list(MyUser.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        #print(temp.role)
        return render(request, "viewuser.html", {'print': x, 'current': temp})

    def post(self, request):
        print('hi3')
        search = request.POST.get('n')
        print(search)
        try:
            user = MyUser.objects.get(name=search)
            MyUser.objects.filter(name=search).delete()
        except MyUser.DoesNotExist:
            return HttpResponse("No such user")
        x = list(MyUser.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        # print(temp.role)
        return render(request, "viewuser.html", {'print': x, 'current': temp})


class CreateUser(View):
    def get(self, request):
        return render(request, "createuser.html", {})

    def post(self, request):
        n = request.POST.get('name')
        p = request.POST.get('password')
        r = request.POST.get('role')
        x = request.POST.get('phone')
        y = request.POST.get('address')
        if n != '' or p != '' or r != '':
            newUser = MyUser(name=n, password=p, role=r, phoneNumber=x, address=y)
            newUser.save()
        return redirect('/home/viewuser.html')


class ViewCourses(View):
    def get(self, request):
        x = list(MyCourses.objects.all())
        if x is None:
            return render(request, "viewcourse.html", {"print": "No Courses have been created yet!"})
        return render(request, "viewcourse.html", {"print": x})

    def post(self, request):
        return render(request, "viewcourse.html", {})


class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        n = request.POST.get('name')
        s = int(request.POST.get('section'))
        i = request.POST.get('instruct')
        t = request.POST.get('ta')
        if n != '':
            newCourse = MyCourses(courseName=n, courseSection=s, courseInstructor=i, courseTA=t)
            newCourse.save()
            return redirect('/home/viewcourse.html')
