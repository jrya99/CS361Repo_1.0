from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)


class Courses(models.Model):
    courseName = models.CharField(max_length=20)

