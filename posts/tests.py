from django.urls import resolve
from django.test import TestCase
from posts.views import home_page



class HomePageTest(TestCase):

    def test_roo_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
