from django.test import TestCase
from django.test import Client
from PurplePanda.models import MyUser
from PurplePanda.assignment import Assignment


class AcceptanceTA(TestCase):

   def setUp(self):
        self.client = Client()
        self.user1 = MyUser.objects.create(name='Patrick', password='Star', role='TA',
                                         phoneNumber='2622622626', address='ChickFilA')
        self.user2 = MyUser.objects.create(name='Spongebob', password='Squarepants', role='TA',
                                         phoneNumber='1234567890', address='Wendys')
        self.user3 = MyUser.objects.create(name='Patrick', password='Stars', role='TA',
                                         phoneNumber='2622622626', address='McDonalds')
        self.assignment1 = Assignments.objects.create(name='Homework 1', date='11/5')
        self.assignment2 = Assignments.objects.create(name='Homework 2', date='12/7')
        self.assignment3 = Assignments.objects.create(name='Homework 3', date='bad due date')


    def test_valid_login(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star'})
        self.assertEqual(response.url, "/home")

    def test_valid_invalid_login(self):
        response = self.client.post('/', {"name": "Spongebob", "password": "Star"})
        self.assertEqual(response.context['message'], "Incorrect Password")

    def test_valid_view_assignments(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star', 'role': 'TA'})
        self.assertEqual(response.url, "/home")

        response = self.client.get('/assignments/', {'username': self.user1.username})
        self.assertEqual(response.context['error'], 'No assignments exist yet...')

        response = self.client.get('/assignments/', {'username': self.user1.username})
        all_assignments = []

        for i in response.context['assignments']:
            all_assignments.append(str(i))
        self.assertEqual(all_assignments, [str(self.assignment1)])

    def test_invalid_view_assignments(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star', 'role': 'TA'})
        self.assertEqual(response.url, "/home")

        response = self.client.get('/assignments/', {'username': self.user1.username})
        self.assertEqual(response.context['error'], 'No assignments exist yet...')



    def test_valid_obtain_info(self):
        response = self.client.post('/', {'name': 'Spongebob', 'password': 'Squarepants'})
        self.assertEqual(response.url, "/contactinfo")

        response = self.client.get('/', {'name': 'Spongebob', 'password': 'Squarepants'})
        self.assertEqual(response.context['contact_info'], [self.user2.name])
