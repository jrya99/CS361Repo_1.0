from django.db import models


class MyUser(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    phoneNumber = models.CharField(max_length=10, default=None, null=True)
    address = models.CharField(max_length=30, default=None, null=True)

    def __str__(self):
        return self.name, self.password, self.role


class MyCourses(models.Model):
    courseName = models.CharField(max_length=20)
    courseSection = models.IntegerField(default=0)
    courseInstructor = models.CharField(max_length=50, default=None)
    courseTA = models.CharField(max_length=50, default=None)

    def __str__(self):
        return self.courseName

