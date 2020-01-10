from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from posts.models import Post

import time

MAX_WAIT = 10

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser_find_tag_name = self.browser.find_element_by_tag_name
        self.browser_find_tag_names = self.browser.find_elements_by_tag_name
        Post.objects.create(title='About python',
                            content='Python is a Programming language')
        Post.objects.create(title='About perl',
                            content='Perl is a Programming language')

    def tearDown(self):
        self.browser.quit()

    def wait_home_page_post_text(self, title_text, content_text):
        start_time = time.time()
        while True:
            try:
                titles = self.browser_find_tag_names('h2')
                self.assertIn(title_text,
                              [title.text for title in titles])
                contents = self.browser_find_tag_names('p')
                self.assertIn(content_text,
                              [content.text for content in contents])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_view_posts_list_and_detail(self):
        # Open a web
        self.browser.get(self.live_server_url)

        # Saw title and header was blog
        self.assertIn('Blog', self.browser.title)
        header_text = self.browser_find_tag_name('h1').text
        self.assertIn('Blog', header_text)

        # See frist post title and content
        self.wait_home_page_post_text('About python',
                                      'Python is a Programming language')

        # See second post title and content
        self.wait_home_page_post_text('About perl',
                                      'Perl is a Programming language')

        # Click the "more" to see the detail
        self.browser.find_element_by_link_text('more').click()

        # browser redirect to detail
        self.assertRegex(self.browser.current_url, '/posts/.+')

        # Read the detail
        title_text = self.browser_find_tag_name('h2').text
        content_text = self.browser_find_tag_name('p').text

        self.assertIn('About python', title_text)
        self.assertIn('Python is a Programming language', content_text)

        self.assertNotIn('About perl', title_text)
        self.assertNotIn('Perl is a Programming language', content_text)
        # Exit


class RestAPIPageTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser_find_tag_name = self.browser.find_element_by_tag_name
        self.browser_find_id = self.browser.find_element_by_id

    def tearDown(self):
        self.browser.quit()

    def wait_api_return_text(self, data_text):
        start_time = time.time()
        while True:
            try:
                return_text = self.browser_find_tag_name('body').text
                self.assertIn(data_text, return_text)
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def wait_input_box_after_enter_data(self, **arg):
        start_time = time.time()
        while True:
            try:
                method = self.browser_find_id('id_method')
                url = self.browser_find_id('id_url')
                input_name = self.browser_find_id('id_input_name')
                input_data = self.browser_find_id('id_input_data')
                add= self.browser_find_id('id_add')
                enter = self.browser_find_id('id_enter')

                method.send_keys(arg['method'])
                url.send_keys(arg['url'])

                try:
                    title_text = arg['title']
                    content_text = arg['content']
                    input_name.send_keys('title_text')
                    input_data.send_keys(title_text)
                    add.click()
                    input_name.send_keys('content_text')
                    input_data.send_keys(content_text)
                    add.click()
                except KeyError:
                    pass
                finally:
                    enter.click()

                return

            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_view_reset_api_page(self):
        # Connect API home page
        self.browser.get(self.live_server_url + '/api')

        # See Blog API
        self.assertIn('Blog API', self.browser.title)
        api_text = self.browser_find_tag_name('h1').text
        self.assertIn('Blog API', api_text)

        # Get post lists
        self.wait_input_box_after_enter_data(method='GET',
                                             url='/api/posts')

        # See posts list but no post
        self.wait_api_return_text('[]')

        # Back to API home page
        self.browser.get(self.live_server_url + '/api')

        # POST first post
        self.wait_input_box_after_enter_data(
            method='POST',
            url='/api/posts',
            title='About python',
            content='Python is a Programming language'
        )

        # browser redirect to url/posts/id/
        self.assertRegex(self.browser.current_url, '/api/posts/.+')

        # See new post data
        self.wait_api_return_text('About python')
        self.wait_api_return_text('Python is a Programming language')

        # Back to API home page
        self.browser.get(self.live_server_url + '/api')

        # POST second post
        self.wait_input_box_after_enter_data(
            method='POST',
            url='/api/posts',
            title='About perl',
            content='Perl is a Programming language'
        )

        # browser redirect to url/posts/id/
        self.assertRegex(self.browser.current_url, '/api/posts/.+')

        # See post data two
        self.wait_api_return_text('About perl')
        self.wait_api_return_text('Perl is a Programming language')

        # Connect posts api page
        self.browser.get(self.live_server_url + '/api/posts')

        # See two posts data
        self.wait_api_return_text('About python')
        self.wait_api_return_text('Python is a Programming language')

        self.wait_api_return_text('About perl')
        self.wait_api_return_text('Perl is a Programming language')

        # Exit
