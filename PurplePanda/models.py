from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.name, self.password, self.role


class Courses(models.Model):
    courseName = models.CharField(max_length=20)

