from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from posts.views import home_page, api_page, posts_api_page
from posts.models import Post


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # html = response.content.decode('utf8')
        self.assertContains(response, 'Blog')


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


class LvieViewTest(TestCase):

    def test_display_all_posts(self):
        Post.objects.create(title='Post title', content='Post content')

        response = self.client.get('/')

        self.assertContains(response, 'Post title')
        self.assertContains(response, 'Post content')


class LiveAPITest(TestCase):

    def test_return_api_home_page(self):
        found = resolve('/api')
        self.assertEqual(found.func, api_page)

    def test_return_api_post_page(self):
        found = resolve('/api/posts')
        self.assertEqual(found.func, posts_api_page)

    def test_get_all_post_lists(self):
        post = Post.objects.create(title='GET title',
                                   content='GET content')
        response = self.client.get('/api/posts')

        self.assertContains(response, post.title)
        self.assertContains(response, post.content)

    def test_post_a_post(self):
        response = self.client.post(
                       '/api/posts',
                       data={'title_text': 'POST title',
                             'content_text': 'POST content'},
                       follow=True
                   )

        self.assertContains(response, 'POST title')
        self.assertContains(response, 'POST content')

    def test_get_one_post_list(self):
        post = Post.objects.create(title='GET one title',
                                   content='GET one content')
        response = self.client.get('/api/posts/1')

        self.assertContains(response, post.title)
        self.assertContains(response, post.content)

    def test_delete_one_post(self):
        post = Post.objects.create(title='DELETE one title',
                                   content='DELETE one content')
        response = self.client.delete('/api/posts/1')

        self.assertNotContains(response, post.title)
        self.assertNotContains(response, post.content)

    def test_put_one_post(self):
        old_response = self.client.put(
                           '/api/posts/1',
                           data={'title_text': 'Old PUT title',
                                 'content_text': 'Old PUT content'}
                       )

        self.assertContains(old_response, 'Old PUT title')
        self.assertContains(old_response, 'Old PUT content')


        new_response = self.client.put(
                           '/api/posts/1',
                           data={'title_text': 'New PUT title',
                                 'content_text': 'New PUT content'}
                       )

        self.assertContains(new_response, 'New PUT title')
        self.assertContains(new_response, 'New PUT content')
        self.assertNotContains(new_response, 'Old PUT title')
        self.assertNotContains(new_response, 'Old PUT content')


    def test_patch_one_post(self):
        old_response = self.client.patch(
                           '/api/posts/1',
                           data={'title_text': 'Old PATCH title',
                                 'content_text': 'Old PATCH content'}
                       )

        self.assertContains(old_response, 'Old PATCH title')
        self.assertContains(old_response, 'Old PATCH content')


        new_response = self.client.patch(
                           '/api/posts/1',
                           data={'title_text': 'New PATCH title'}
                       )

        self.assertContains(new_response, 'New PATCH title')
        self.assertContains(new_response, 'Old PATCH content')
        self.assertNotContains(new_response, 'Old PATCH title')

