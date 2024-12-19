from django.test import TestCase
from django.shortcuts import reverse


class PublicHomePagesTest(TestCase):
    def test_200_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_200_homepage_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


    def test_200_aboutus(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_200_aboutus_by_name(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)