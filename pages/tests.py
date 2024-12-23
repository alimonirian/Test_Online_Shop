from django.test import TestCase
from django.shortcuts import reverse


class PublicHomePagesTest(TestCase):
    def test_homepage_by_urls_200(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_url_by_name_200(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_content(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Home Page')


    def test_aboutus_by_urls_200(self):
        response = self.client.get('/aboutus/')
        self.assertEqual(response.status_code, 200)

    def test_aboutus_by_name_200(self):
        response = self.client.get(reverse('aboutus'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_content(self):
        response = self.client.get(reverse('aboutus'))
        self.assertContains(response, 'About Us')
