import unittest
from django.test import TestCase
from PurplePandaProject.PurplePandaProject.Classes.Admin import Admin
from PurplePandaProject.PurplePandaProject.Classes.Parent import Parent


class AdminTest(TestCase):

    def setup(self):
        self.b = ("John", "Johnson")
        self.c = ("Jake", "Ryan", "Admin", "void")
        self.d = "Jack"
        self.x = ("John", 123, "Admin")

    def test_oneArg(self):
        with self.assertRaises(TypeError, "Cannot have only one argument"):
            a = Admin.__init__(self.d)

    def test_twoArg(self):
        with self.assertRaises(TypeError, "Cannot have only two arguments"):
            a = Admin.__init__(self.b)

    def test_fourArg(self):
        with self.assertRaises(TypeError, "Cannot have more than three arguments"):
            a = Admin.__init__(self.c)

    def test_invalidArg(self):
        with self.assertRaises(TypeError, "Incorrect parameter type"):
            a = Admin.__init__(self.x)

    def create_TestParam(self):
        with self.assertRaises(TypeError, "When calling create_class must pass in correct param"):
            a = Admin.create_class(0, 0)

    def create_OneParam(self):
        with self.AssertRaises(TypeError, "Must have more than one argument to call create_class"):
            a = Admin.create_class("test")

    def create_MoreParam(self):
        with self.AssertRaises(TypeError, "Can't have more than two arguments when calling create_class"):
            a = Admin.create_class("test", "test", "test")