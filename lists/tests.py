from django.test import TestCase


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        # request = HttpRequest()
        # response = home_page(request)
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
