from django.test import TestCase
from django.test.client import Client
from users.models import User
from django.core.management import call_command


class TestUserManagement(TestCase):
    success = 200
    redirect = 302

    def setUp(self):
        self.user = User.objects.create_superuser('django', 'django@geekshop.local', 'geekbrains')
        self.client = Client()

    def test_user_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.success)
        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username='django', password='geekbrains')

        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.redirect)

    def tearDown(self):
        call_command('sqlsequencereset', 'products', 'users', 'orders', 'baskets')
