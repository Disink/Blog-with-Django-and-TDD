from django.test import LiveServerTestCase
from selenium import webdriver


class NewVivitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_view_posts_list_and_detail(self):
        #self.browser.get('http://localhost:8000')
        # Open a web
        self.browser.get(self.live_server_url)

        # Saw title and header was blog
        self.assertIn('blog', self.browser.title)
        header_text = self.borwser.find_element_by_tag_name('h1').text
        self.assertIn('blog', header_text)

        # Saw the title of an article

        # Saw the summary of an article

        # Click the "more" to see the detail

        # Exit web after reading the detail
