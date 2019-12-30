from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from posts.views import home_page



class HomePageTest(TestCase):

    def test_roo_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # html = response.content.decode('utf8')
        self.assertContains(response, 'blog')

