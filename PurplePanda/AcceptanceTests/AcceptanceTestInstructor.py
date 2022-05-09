from django.test import TestCase
from django.test import Client
from PurplePandaProject.PurplePandaApp.Classes import Assignment
from PurplePandaProject.PurplePandaApp.Classes import Instructor
from PurplePandaProject.PurplePandaApp.Classes import TA

class TestAcceptanceInstructor(TestCase):
    def setup(self):
        self.client = Client()
        self.user1 = Instructor.Instructor(username="user1",password="Password1")
        self.user2 = Instructor.Instructor(username="user2", password="Password2")
        self.a1 = ("HW1","12/25")
        self.assignment1 = Assignment(self.a1)
        self.assignments = {"assignment1": [self.assignment1.name, self.assignment1.date]}
        self.userTA = TA.TA(username="TAuser", password="TApassword")

    def test_valid_login(self):
        response = self.client.post('/', {"name": "user1", "password": "Password1"})
        self.assertEqual(response.url, "/things/", msg="Did not login correctly")

    def test_valid_login2(self):
        response = self.client.post('/', {"name": "user2", "password": "Password2"})
        self.assertEqual(response.url, "/things/", msg="Did not login correctly")

    def test_invalid_login(self):
        response = self.client.post('/', {"name": "user1", "password": "passwooo88"})
        self.assertEqual(response.context["message"], "Incorrect Password", msg="invalid login")

    def test_invalid_login2(self):
        response = self.client.post('/', {"name": "user2", "password": "Password1"})
        self.assertEqual(response.context["message"], "Incorrect Password", msg="invalid login")

    def test_view_assignments(self):
        response = self.user1.view_assignments(assignments=self.assignments)
        self.assertEqual(response.context["things"], self.assignment1.name + self.assignment1.date, msg="did not view assignments correctly")

    def test_assignTA(self):
        self.user2.assigning_ta(lab_id="TEST123", username=self.userTA.username)
        self.assertEqual(self.user2.lab_ta[0], {"lab_id":"TEST123", "username":self.userTA.username}, msg="error occurred while assigning TA")

    def test_password_change(self):
        self.user1.set_password("PasswordChange1")
        self.assertEqual("PasswordChange1", self.user1.get_password(), msg="New password was not setup correctly")
        self.user1.set_password("Password1")
