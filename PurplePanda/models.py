from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=10, default=None, null=True)
    address = models.CharField(max_length=30, default=None, null=True)

    def __str__(self):
        return self.name, self.password, self.role
    
    def set_name(self, name):
        self.name = name

    def set_password(self, password):
        self.password = password

    def set_role(self, role):
        self.role = role

    def set_phoneNumber(self, phoneNumber):
        self.phoneNumber = phoneNumber

    def set_address(self, address):
        self.address = address

class Assignments(models.Model):
    name = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    assignments = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def set_name(self, name):
        self.name = name

    def set_date(self, date):
        self.date = date

    def set_assignments(self, assignments):
        self.assignments = assignments;

    def __str__(self):
        return self.name, self.date, self.assignments

class MyCourses(models.Model):
    courseName = models.CharField(max_length=20)
    courseSection = models.CharField(max_length=20)
    courseInstructor = models.CharField(max_length=50, default=None)
    courseTA = models.CharField(max_length=50, default=None)

    def setInstructor(self, string):
        self.courseInstructor = string

    def setTA(self, string):
        self.courseTA = string

    def __str__(self):
        return self.courseName

