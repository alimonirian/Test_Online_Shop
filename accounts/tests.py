from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse_lazy


class SignUpPageTest(TestCase):
    username = 'MyUsername'
    email = 'myusername@gmail.com'

    def test_signup_page_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_url(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_signup_contain(self):
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Sign Up')

    def test_signup_form(self):
        user = get_user_model().objects.create_user(
            self.username,
            self.email,
        )
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)


class LogInPageTest(TestCase):
    username = 'MyUsername'
    password = 'MyPassword'
    email = 'myusername@gmail.com'

    def setUp(self):
        """Set up a user for testing."""

        # Create a user to be used in tests
        # self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        user = get_user_model().objects.create_user(
            self.username,
            self.password,
            self.email,
        )

    def test_login_page_url_by_name(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_page_url(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_contain(self):
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Login')

    def test_login(self):
        c = Client()
        c.login(username=self.username, password=self.password)
        c.logout()

    def test_successfully_login(self):
        response = self.client.post(reverse_lazy('login'), username=self.username, password=self.password)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))