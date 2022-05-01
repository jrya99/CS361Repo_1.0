from django.test import TestCase
from django.test import Client
from PurplePanda.models import User
from PurplePanda.assignment import Assignment


class AcceptanceTA(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(name='Patrick', password='Star')
        self.user2 = User.objects.create(name='Spongebob', password='Squarepants')
        self.user3 = User.objects.create(name='Patrick', password='Stars')
        self.assignment1 = Assignment.objects.create(name='Homework 1', date='11/5')
        self.assignment2 = Assignment.objects.create(name='Homework 2', date='12/7')
        self.assignment3 = Assignment.objects.create(name='Homework 3', date='bad due date')
        self.list = {"assignment1": [self.assignment1.name, self.assignment1.date],
                     "assignment2":[self.assignment2.name, self.assignment1.date]}
        self.invalid_list = {"assignment1": [self.assignment1.name, self.assignment1.date],
                     "assignment3":[self.assignment3.name, self.assignment3.date]}


    def test_valid_login(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star'})
        self.assertEqual(response.url, "/things")

    def test_valid_invalid_login(self):
        response = self.client.post('/', {"name": "Spongebob", "password": "Star"})
        self.assertEqual(response.context['message'], "Incorrect Password")

    def test_valid_view_assignments(self):
   #     response = self.client.post('/', {'name': 'Spongebob', 'password': 'Squarepants'})
   #     self.assertEqual(response.url, "/things")

     #   response = self.client.get('/assignments/', {'name': self.assignment1.name, 'date': self.assignment1.date})

      #  self.assertEqual(response.context['things'], [self.assignment1.name, self.assignment1.date])


        for i in self.list.keys():
            resp = self.client.post("/", {"name": i, "date": i})
            self.assertEqual(resp.url, "/things/")

            resp = self.client.post('/things/', {'name': self.assignment1.name})
            self.assertEqual(len(resp.context['things']), len(self.thingList[i])+1)
            self.assertEqual(resp.context['things'], self.thingList[i] + [self.assignment1.name])

    def test_invalid_view_assignments(self):

    def test_valid_obtain_info(self):
        response = self.client.post('/', {'name': 'Spongebob', 'password': 'Squarepants'})
        self.assertEqual(response.url, "/things")

        response = self.client.get('/', {'name': 'Spongebob', 'password': 'Squarepants'})

        self.assertEqual(response.contect['things'], [self.user2.name])
