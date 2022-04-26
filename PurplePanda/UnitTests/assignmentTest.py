import unittest
import datetime
from PurplePandaProject.PurplePandaProject.Classes.Assignment import Assignment


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Assignment('assignment1', datetime.date(2025, 5, 15))
        self.b = Assignment('assignment2')
        self.c = Assignment('assignment3', datetime.date(2025, 5, 15), 'thirdField')
        self.d = Assignment(datetime.date(2025, 5, 15))
        self.e = Assignment()
        self.f = 'assignment4'
        self.invalid_name = (123, datetime.date(2025, 5, 15))
        self.invalid_date = ('assignment5', 'date')
        self.two_null_arg = Assignment(None, None)
        self.null_date_arg = Assignment('assignment6', None)
        self.null_name_arg = Assignment(None, 2025, 5, 15)
        self.today_date = Assignment('assignment7', datetime.date.today)

    def test_oneArg(self):
        with self.assertRaises(TypeError, msg="Cannot have only one argument"):
            a = Assignment.__init__(self.e)

    def test_twoArg(self):
        with self.assertRaises(TypeError, msg="Cannot have only two arguments"):
            a = Assignment.__init__(self.b)

    def test_fourArg(self):
        with self.assertRaises(TypeError, msg="Cannot have more than three arguments"):
            a = Assignment.__init__(self.c)

    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="Incorrect parameter type"):
            a = Assignment.__init__(self.invalid_name)
            a = Assignment.__init__(self.invalid_date)

    def test_nullArg(self):
        with self.assertRaises(TypeError, msg="Cannot have null arguments"):
            a = Assignment.__init__(self.two_null_arg)
            a = Assignment.__init__(self.null_date_arg)
            a = Assignment.__init__(self.null_name_arg)