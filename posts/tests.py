from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from posts.views import home_page
from posts.models import Post



class HomePageTest(TestCase):

    def test_roo_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # html = response.content.decode('utf8')
        self.assertContains(response, 'blog')

class PostModelsTest(TestCase):

    def test_saving_and_retrieving_items(self):
        Post.objects.create(title='First title', content='First content')
        Post.objects.create(title='Second title', content='Second content')

        saved_post = Post.objects.all()
        self.assertEqual(saved_post.count(), 2)

        first_saved_post = saved_post[0]
        second_saved_post = saved_post[1]

        self.assertEqual(first_saved_post.title, 'First title')
        self.assertEqual(first_saved_post.content, 'First content')
        self.assertEqual(second_saved_post.title, 'Second title')
        self.assertEqual(second_saved_post.content, 'Second content')
