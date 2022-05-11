from django.shortcuts import render, redirect
from django.views import View
from PurplePanda.models import MyUser, MyCourses, UserMessages
from django.shortcuts import HttpResponse


class Login(View):
    def get(self, request):
        return render(request, "../static/../templates/login.html", {})

    def post(self, request):
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
                return redirect("/viewuser/")


class ViewCourses(View):
    def get(self, request):
        x = list(MyCourses.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        if x is None:
            return render(request, "viewcourse.html", {"print": "No Courses have been created yet!", "current": temp})
        return render(request, "viewcourse.html", {"print": x, "current": temp})

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
            return render(request, "createcourse.html", {"message":"Course Section already exists"})
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
            return redirect("/viewcourse/")


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


class AssignInstructor(View):
    def get(self, request):
        courses = MyCourses.objects.all()
        users = MyUser.objects.all()
        return render(request, 'assigninstructor.html', {'courses': courses, 'users': users})

    def post(self, request):
        all_courses = MyCourses.objects.all()
        all_users = MyUser.objects.all()

        course = request.POST.get('course_name')
        section = request.POST.get('section')
        new_instruct = request.POST.get('instructor')

        if section == '' or section is None:
            return render(request, 'assigninstructor.html', {'courses': all_courses, 'users': all_users, 'message': 'You didnt enter in the course section'})

        for x in all_courses:
            if x.courseName == course and x.courseSection == section:
                temp = MyCourses.objects.get(courseName=x.courseName, courseSection=x.courseSection)
                temp.courseInstructor = new_instruct
                temp.save()
                return redirect("/viewcourse/")

        return render(request, 'assigninstructor.html', {'courses': all_courses, 'users': all_users, 'message': 'The section you entered doesnt exist in the course'})


class AssignTA(View):
    def get(self, request):
        courses = MyCourses.objects.all()
        users = MyUser.objects.all()
        return render(request, 'assignta.html', {'courses': courses, 'users': users})

    def post(self, request):
        all_courses = MyCourses.objects.all()
        all_users = MyUser.objects.all()

        course = request.POST.get('course_name')
        section = request.POST.get('section')
        new_ta = request.POST.get('ta')

        if section == '' or section is None:
            return render(request, 'assignta.html', {'courses': all_courses, 'users': all_users,
                                                             'message': 'You didnt enter in the course section'})

        for x in all_courses:
            if x.courseName == course and x.courseSection == section:
                temp = MyCourses.objects.get(courseName=x.courseName, courseSection=x.courseSection)
                temp.courseTA = new_ta
                temp.save()
                return redirect("/viewcourse/")

        return render(request, 'assignta.html', {'courses': all_courses, 'users': all_users,
                                                         'message': 'The section you entered doesnt exist in the course'})


class ViewMessage(View):
    def get(self, request):
        x = list(UserMessages.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        return render(request, 'viewmessage.html', {'print': x, 'current': temp})

    def post(self, request):
        x = list(UserMessages.objects.all())
        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        return render(request, 'viewmessage.html', {'print': x, 'current': temp})


class OpenMessage(View):
    def get(self, request):
        return render(request, 'openmessage.html', {})


class SendMessage(View):
    def get(self, request):
        return render(request, 'sendmessage.html', {})

    def post(self, request):
        receiver = request.POST.get('receiver')
        subject = request.POST.get('subject')
        body = request.POST.get('body')
        if receiver is None or subject is None:
            return render(request, 'sendmessage.html', {{ 'message': 'You cannot leave receiver or subject blank'}})

        temp = request.session.get("name")
        temp = MyUser.objects.get(name=temp)
        get_receiver = MyUser.objects.get(name=receiver)
        new_message = UserMessages(sender=temp, receiver=get_receiver, subject=subject, body=body, read=False)
        new_message.save()
        return redirect("/viewmessage/")
