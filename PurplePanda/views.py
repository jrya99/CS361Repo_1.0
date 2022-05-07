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
        except MyUser.DoesNotExist:
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
        x = list(MyUser.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        #print(temp.role)
        return render(request, "viewuser.html", {'print': x, 'current': temp})

    def post(self, request):
        search = request.POST.get('n')
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
        try:
            user = MyUser.objects.get(name=n)
            return render(request, 'createuser.html', {'message': "User already exists"})
        except MyUser.DoesNotExist:
            if n != '' or p != '' or r != '':
                newUser = MyUser(name=n, password=p, role=r, phoneNumber=x, address=y)
                newUser.save()
                x = list(MyUser.objects.all())
                temp = request.session.get("name")
                temp = MyUser.objects.get(name=temp)
                return render(request,'viewuser.html',{'print':x,'current':temp})


class ViewCourses(View):
    def get(self, request):
        x = list(MyCourses.objects.all())
        if x is None:
            return render(request, "viewcourse.html", {"print": "No Courses have been created yet!"})
        return render(request, "viewcourse.html", {"print": x})

    def post(self, request):
        search = request.POST.get('n')
        search2 = request.POST.get('s')
        try:
            course = MyCourses.objects.get(courseName=search, courseSection=search2)
            course.delete()
        except MyCourses.DoesNotExist:
            return HttpResponse("No such course")
        x = list(MyCourses.objects.all())
        if x is None:
            return render(request, "viewcourse.html", {"print": "No Courses have been created yet!"})
        return render(request, "viewcourse.html", {"print": x})


class CreateCourse(View):
    def get(self, request):
        return render(request, "createcourse.html", {})

    def post(self, request):
        n = request.POST.get('name')
        s = request.POST.get('section')
        i = request.POST.get('instruct')
        t = request.POST.get('ta')
        try:
            course = MyCourses.objects.get(courseName=n, courseSection=s)
            return render(request,"createcourse.html", {"message":"Course Section already exists"})
        except MyCourses.DoesNotExist:
            if n != '' and s != '':
                newCourse = MyCourses(courseName=n, courseSection=s, courseInstructor=i, courseTA=t)
                if t == '':
                    newCourse.setTA('TBA')
                if i == '':
                    newCourse.setInstructor('TBA')
                newCourse.save()
            else:
                return render(request, "createcourse.html", {"message":"Course Name and Section fields cannot be empty"})
            x = list(MyCourses.objects.all())
            if x is None:
                return render(request, "viewcourse.html", {"print": "No Courses have been created yet!"})
            return render(request,'viewcourse.html',{"print": x})


class Profile(View):
    def get(self, request):
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        return render(request, "profile.html", {'current': temp, 'message': ''})

    def post(self, request):
        n = request.POST.get('name')
        x = request.POST.get('number')
        y = request.POST.get('address')
        p = request.POST.get('password')
        if n!='':
            try:
                user = MyUser.objects.get(name=n)
                temp = request.session.get("name")
                temp = MyUser.objects.get(name=temp)
                return render(request, 'profile.html', {'current': temp, 'message': "Username already exists"})
            except MyUser.DoesNotExist:
                temp = request.session.get("name")
                temp = MyUser.objects.get(name=temp)
                request.session.__setitem__('name', n)
                temp.name = n
                if p != '':
                    temp.password = p
                if x != '':
                    temp.phoneNumber = x
                if y != '':
                    temp.address = y
                temp.save()
                return render(request, 'profile.html', {'current': temp, 'message': ''})
        else:
            temp = request.session.get("name")
            temp = MyUser.objects.get(name=temp)

            if p != '':
                temp.password = p

            if x != '':
                temp.phoneNumber = x
            if y != '':
                temp.address = y
            temp.save()
            return render(request, 'profile.html', {'current': temp, 'message': ''})


