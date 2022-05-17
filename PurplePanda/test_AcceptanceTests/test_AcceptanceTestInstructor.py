from django.test import TestCase
from django.test import Client
from PurplePanda.models import MyUser, Assignments

class TestAcceptanceInstructor(TestCase):

    def setup(self):
        self.client = Client()
        self.user1 = MyUser.objects.create(name='Patrick', password='Star', role='Instructor',
                                         phoneNumber='2622622626', address='ChickFilA')
        self.user2 = MyUser.objects.create(name='Spongebob', password='Squarepants', role='Instructor',
                                         phoneNumber='1234567890', address='Wendys')
        self.user3 = MyUser.objects.create(name='Patrick', password='Stars', role='Instructor',
                                         phoneNumber='2622622626', address='McDonalds')

        self.assignment1 = Assignments.objects.create(name='Homework 1', date='11/5')
        self.assignment2 = Assignments.objects.create(name='Homework 2', date='12/7')
        self.assignment3 = Assignments.objects.create(name='Homework 3', date='bad due date')
        self.assignments = {"assignment1": [self.assignment1.name, self.assignment1.date]}

        self.user1 = MyUser.objects.create(name='Squilliams', password='Mermaid', role='TA',
                                         phoneNumber='1000000000', address='Popeyes')

    def test_valid_login(self):
        response = self.client.post('/', {"name": "user1", "password": "Password1"})
        self.assertEqual(response.url, "/home/")

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
