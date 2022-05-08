from django.test import TestCase
from django.test import Client
from PurplePanda.models import User


class AcceptanceAdmin(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = User.objects.create(name='Patrick', password='Star', role='Administrator', phoneNumber='2622622626', address='ChickFilA')
        self.user2 = User.objects.create(name='Sandy', password='Cheeks', role='TA', phoneNumber='1234567890', address='BikiniBottom')

    def test_valid_login(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star', 'role': 'Administrator'})
        self.assertEqual(response.url, "/home")

    def test_valid_invalid_login(self):
        response = self.client.post('/', {"name": "Spongebob", "password": "Star", 'role': 'Administrator'})
        self.assertEqual(response.context['message'], "Incorrect Password")

    def test_create_user(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star', 'role': 'Administrator'})
        self.assertEqual(response.url, "/home")

        response = self.client.post('/create_users/', {'name': self.user2.username, 'password': None, 'role': 'TA'})
        all_users = {}

        for i in response.context['users']:
            all_users.update(str(i))
        self.assertEqual(all_users, {'name': self.user2.username, 'password': None, 'role': 'TA'})

    def test__invalid_create_user(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star', 'role': 'Administrator'})
        self.assertEqual(response.url, "/home")

        response = self.client.post('/create_users/', {'name': self.user2.username, 'password': None, 'role': 'TA'})

        self.assertEqual(response.context['message'], "invalid username, password, or role")

        #delete course and delete section

