from django.test import LiveServerTestCase
from selenium import webdriver

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

        # See Blog API
        self.assertIn('Blog API', self.browser.title)
        api_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog API', api_text)

        # See three input box
        first_method = self.browser.find_element_by_id('id_method')
        first_url = self.browser.find_element_by_id('id_url')
        first_enter = self.browser.find_element_by_id('id_enter')

        # Input GET, url/posts
        first_method.send_keys('GET')
        first_url.send_keys('/api/posts')

        # Input Enter
        first_enter.click()

        # See posts list but no post
        first_api_return_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('[]', first_api_return_text)

        # Back to API home page
        self.browser.get(self.live_server_url + '/api')

        # See three input box
        second_method = self.browser.find_element_by_id('id_method')
        second_url = self.browser.find_element_by_id('id_url')
        second_input_name = self.browser.find_element_by_id('id_input_name')
        second_input_data = self.browser.find_element_by_id('id_input_data')
        second_add= self.browser.find_element_by_id('id_add')
        second_enter = self.browser.find_element_by_id('id_enter')

        # Input POST, url/posts, Post data
        second_method = self.browser.find_element_by_id('id_method')
        second_method.send_keys('POST')
        second_url.send_keys('/api/posts')
        second_input_name.send_keys('title_text')
        second_input_data.send_keys('About Python')
        second_add.click()
        second_input_name.send_keys('content_text')
        second_input_data.send_keys('Python is a Programming language')
        second_add.click()

        # Input Enter
        second_enter.click()

        # See new post data
        second_api_return_text = self.browser.find_element_by_tag_name('body').text
        second_posts_data = str([{'id': 1, 'title': 'About Python',
                                'content': 'Python is a Programming language'}])
        self.assertIn(second_api_data, second_api_return_text)

        # See url change to url/posts/1

        # Input POST again

        # See new post data

        # See url change to url/posts/2

        # Connect posts api page

        # See two posts data

        # Back to API home page

        # Input DELETE, url/posts/1

        # Connect posts api page

        # See only one post
