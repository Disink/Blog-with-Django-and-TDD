from django.test import LiveServerTestCase
from selenium import webdriver
from seleniumrequests import Firefox

from posts.models import Post

import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.post = Post.objects.create(title='About python', content='Python is a Programming language')

    def tearDown(self):
        self.browser.quit()

    def test_view_posts_list_and_detail(self):
        #self.browser.get('http://localhost:8000')
        # Open a web
        self.browser.get(self.live_server_url)

        # Saw title and header was blog
        self.assertIn('blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('blog', header_text)

        # Saw the title of an article
        post_title = self.browser.find_element_by_tag_name('h2').text
        self.assertIn('About python', post_title)

        # Saw the summary of an article
        post_summary = self.browser.find_element_by_tag_name('p').text
        self.assertIn('Python is a Programming language', post_summary)

        # Click the "more" to see the detail

        # Exit web after reading the detail


class RestAPIPageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_view_reset_api_page(self):
        # Connect API home page
        self.browser.get(self.live_server_url + '/api')

        # Saw Blog API
        self.assertIn('Blog API', self.browser.title)
        api_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog API', api_text)


class RestAPIMethodsTest(LiveServerTestCase):

    def setUp(self):
        self.browser = Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_use_rest_api(self):
        # Get posts list then retuen None
        response = self.browser.request('GET', self.live_server_url + '/api/posts')
        self.assertIn('None', response.content.decode())

        # Post two post

        # Get one post

        # Get posts list

        # Delete first post


