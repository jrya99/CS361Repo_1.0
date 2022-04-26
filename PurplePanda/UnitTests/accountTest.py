import unittest
from PurplePandaProject.PurplePandaProject.Classes.Account import Account


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a = Account('username', 'password')
        self.b = Account('username')
        self.c = Account('username', 'password', 'thirdArg')
        self.d = Account()
        self.e = 'username'
        self.invalid_username = (123, 'password')
        self.invalid_password = ('username', 123)
        self.two_null_arg = Account(None, None)
        self.null_date_arg = Account('username', None)
        self.null_name_arg = Account(None, 'password')

    def test_oneArg(self):
        with self.assertRaises(TypeError, msg="Cannot have only one argument"):
            a = Account.__init__(self.e)

    def test_twoArg(self):
        with self.assertRaises(TypeError, msg="Cannot have only two arguments"):
            a = Account.__init__(self.b)

    def test_fourArg(self):
        with self.assertRaises(TypeError, msg="Cannot have more than three arguments"):
            a = Account.__init__(self.c)

    def test_invalidArg(self):
        with self.assertRaises(TypeError, msg="Incorrect parameter type"):
            a = Account.__init__(self.invalid_username)
            a = Account.__init__(self.invalid_password)

    def test_nullArg(self):
        with self.assertRaises(TypeError, msg="Cannot have null arguments"):
            a = Account.__init__(self.two_null_arg)
            a = Account.__init__(self.null_date_arg)
            a = Account.__init__(self.null_name_arg)