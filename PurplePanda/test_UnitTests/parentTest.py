import unittest
from PurplePandaProject.PurplePandaProject.Classes.Parent import Parent


class TestInit(unittest.TestCase):
    def setup(self):
        noInput = Parent()
        noneInput = Parent(None, None, None)

    def test_no_input(self):
        self.assertEqual(self.noInput.username, self.noneInput.username, "blank constructor username not none")
        self.assertEqual(self.noInput.password, self.noneInput.password, "blank constructor password not none")
        self.assertEqual(self.noInput.role, self.noneInput.role, "blank constructor role not none")

    def test_too_much_input(self):
        with self.assertRaises(TypeError, msg="too much input in __init__()"):
            fourArg = Parent("klinger", "12345", "Admin", "11111")

    def test_BadDataInt(self):
        with self.assertRaises(TypeError, msg="Invalid argument Int"):
            intArg = Parent(123, 12345, 123)

    def test_BadDataFloat(self):
        with self.assertRaises(TypeError, msg="Invalid argument Float"):
            floatArg = Parent(123.0, 12345.0, 123.0)

    def test_BadData_List(self):
        with self.assertRaises(TypeError, msg="Invalid argument List"):
            listArg = Parent([1, 2, 3], [1, 2, 3, 4, 5], [1, 2, 3])


class TestPasswordUsernameChange(unittest.TestCase):
    def setup(self):
        t1 = Parent("klinger", "12345", "Admin")
        t2 = Parent("john", "11111", "Admin")

    def test_no_input(self):
        with self.asserRaises(TypeError, msg="Not enough input is given in password_username_change()"):
            self.t1.password_username_change()

    def test_too_much_input(self):
        with self.assertRaises(TypeError, msg="too much input in password_username_change()"):
            self.t1.password_username_change("klingerm", "11122", "12345")

    def test_BadData_Int(self):
        with self.asserRaises(TypeError, msg="Invalid int when changing username and password"):
            self.t1.password_username_change(123, 123)

    def testBadData_Float(self):
        with self.assertRaises(TypeError, msg="Invalid Float when changing username and password"):
            self.t1.password_username_change(123.0, 1.0)

    def testBadData_List(self):
        with self.assertRaises(TypeError, msg="Invalid List when changing username and password"):
            self.t1.password_username_change([1, 2, 3], [1, 2, 3])

    def test_correct_change(self):
        self.t2.password_username_change("klinger", "12345")
        self.assertEqual(self.t1.username, self.t2.username, "username not changed correctly")
        self.assertEqual(self.t1.password, self.t2.password, "password not changed correctly")


class TestSetContactInfo(unittest.TestCase):
    def setup(self):
        t1 = Parent("klinger", "12345", "Admin")
        t2 = Parent("john", "11111", "Admin")

    def test_no_set(self):
        self.assertEqual(self.t1.address, None, "address is already setup")
        self.assertEqual(self.t1.email, None, "email is already setup")
        self.assertEqual(self.t1.number, None, "number is already setup")

    def test_no_input(self):
        with self.assertRaises(TypeError, msg="Not enough input in set_contact_info()"):
            self.t1.set_contact_info()

    def test_too_much_input(self):
        with self.assertRaises(TypeError, msg="too much input in set_contact_info()"):
            self.t1.set_contact_info("12345 Milwaukee", "klingerm@uwm.edu", "123-123-1234", "12345")

    def test_BadData_Int(self):
        with self.assertRaises(TypeError, msg="Invalid data int in set_contact_info"):
            self.t1.set_contact_info(123, 123, 123)

    def test_BadData_Float(self):
        with self.assertRaises(TypeError, msg="Invalid data float in set_contact_info"):
            self.t1.set_contact_info(123.0, 123.0, 123.0)

    def test_BadData_List(self):
        with self.assertRaises(TypeError, msg="Invalid data list in set_contact_info"):
            self.t1.set_contact_info([123], [123], [123])

    def test_setUp(self):
        self.t1.set_contact_info("12345 Milwaukee", "klingerm@uwm.edu", "123-123-1234")
        self.assertEqual(self.t1.address, "12345 Milwaukee", "address not changed correctly")
        self.assertEqual(self.t1.email, "klingerm@uwm.edu", "email not changed correctly")
        self.assertEqual(self.t1.number, "123-123-1234", "number not changed correctly")


class TestPrintContactInfo(unittest.TestCase):
    def setup(self):
        t1 = Parent("klinger", "12345", "Admin")
        t1.set_contact_info("12345 Milwaukee", "klingerm@uwm.edu", "123-123-1234")

    def test_input(self):
        with self.assertRaises(TypeError, msg="input in print contact info"):
            self.t1.print_contact_info("thing")

    def test_normal(self):
        self.assertEqual(self.t1.print_contact_info(),
                         "Address: 12345 Milwaukee\nEmail: klingerm@uwm.edu\nPhone Number: 123-123-1234",
                         "information not printed properly")


class TestPrintUserInfo(unittest.TestCase):
    def setup(self):
        t1 = Parent("klinger", "12345", "Admin")

    def test_inupt(self):
        with self.assertRaises(TypeError, msg="input in print user info"):
            self.t1.print_user_info("thing")

    def test_normal(self):
        self.assertEqual(self.t1.print_user_info(), "Username: klinger\nRole: Admin", "user info not printed correctly")


class TestProfileDesign(unittest.TestCase):
    pass


class TestSendNotifications(unittest.TestCase):
    pass