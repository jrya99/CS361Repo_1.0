rom django.test import TestCase
from django.test import Client
from PurplePanda.models import MyUser


class TestLogin(TestCase):

    def setUp(self):
        self.client = Client()
        self.user1 = MyUser.objects.create(name='Patrick', password='Star', role='Admin',
                                           phoneNumber='2622622626', address='ChickFilA')
        self.user2 = MyUser.objects.create(name='Spongebob', password='Squarepants', role='TA',
                                           phoneNumber='1234567890', address='Wendys')
        self.user3 = MyUser.objects.create(name='Mister', password='Krabs', role='Instructor',
                                           phoneNumber='2622622626', address='McDonalds')
        self.user_bad = MyUser.objects.create(name='Mister', password='Krabsss', role='Instructor',
                                              phoneNumber='2622622626', address='McDonalds')

    def test_valid_login1(self):
        response = self.client.post('/', {'name': 'Patrick', 'password': 'Star'})
        self.assertEqual(response.url, "/home")

    def test_valid_invalid_login(self):
        response = self.client.post('/', {"name": "Spongebob", "password": "Star"})
        self.assertEqual(response.context['message'], "Incorrect Password or Username")

    def test_valid_invalid_login2(self):
        response = self.client.post('/', {"name": "Mister", "password": "Star"})
        self.assertEqual(response.context['message'], "Incorrect Password or Username")
