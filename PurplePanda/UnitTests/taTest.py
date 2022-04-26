import unittest
from PurplePandaProject.PurplePandaProject.Classes.TA import TA
from PurplePandaProject.PurplePandaProject.Classes.Parent import Parent

class TATests(unittest.TestCase):

    def setup(self):
        self.a = ("spongebob", "patrick123")
        self.b = ("Mr", "Krabs123")
        self.three_args = ("Sandy", "Cheeks", "Karen")
        self.two_args = ("Sandy", "Cheeks")
        self.one_args = ("Plankton")
        self.fail = (None, None, None)
        self.invalid_int = (123, 345, "TA")
        self.c = 123
        self.d = 12.3
        self.n = None
        self.class1 = "History 101"
        self.class2 = "CS 361"

    def test_oneArg(self):
        with self.assertRaises(TypeError) as context1:
            c = self.one_args
        print(context1.exeption, "1 arguments are not permitted for a user")

    def test_threeArg(self):
        with self.assertRaises(TypeError) as context1:
            c = self.three_args
        print(context1.exeption, "3 arguments are not permitted for a user")

    def valid_username(self):
        result = self.a
        expected = ("spongebob", "patrick123", "TA")
        self.assertEqual(result, expected)

    def null_ta(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.fail
        self.assertEqual(str(context1.exception), "TA must not be null")

    def int_ta(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.invalid_int
        self.assertEqual(str(context1.exception), "TA must not be an int")

    def test_view_assignments_int(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.view_assignments(self.int)
        self.assertEqual(str(context1.exception), "Argument must not be an int")

    def test_view_assignments_double(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.view_assignments(self.d)
        self.assertEqual(str(context1.exception), "Argument must not be an double")

    def test_view_assignments_null(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.view_assignments(self.n)
        self.assertEqual(str(context1.exception), "Argument must not be a Null")

    def test_view_assignments_valid1(self):
        a = self.class1
        expected = "History 101"
        self.assertEqual(a, expected)

    def test_view_assignments_valid2(self):
        a = self.class2
        expected = "CS 361"
        self.assertEqual(a, expected)

    def test_obtain_info_valid1(self):
        self.assertEqual(self.obtain_contact_info(self.a.username), self.a.contact_info)

    def test_obtain_info_valid2(self):
        self.assertEqual(self.obtain_contact_info(self.b.username), self.b.contact_info)

    def test_obtain_info_null(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.obtain_contact_info(self.fail)
        self.assertEqual(str(context1.exception), "Argument must not be a Null")

    def test_obtain_info_int(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.obtain_contact_info(self.c)
        self.assertEqual(str(context1.exception), "Argument must not be an int")

    def test_obtain_info_double(self):
        with self.assertRaises(TypeError) as context1:
            self.result = self.a.obtain_contact_info(self.d)
        self.assertEqual(str(context1.exception), "Argument must not be an double")

    def test_oneArg(self):
        with self.assertRaises(TypeError) as context1:
            c = self.a.obtain_contact_info(self.one_args)
        print(context1.exeption, "1 arguments are not permitted")

    def test_threeArg(self):
        with self.assertRaises(TypeError) as context1:
            c = self.a.obtain_contact_info(self.three_args)
        print(context1.exeption, "3 arguments are not permitted")