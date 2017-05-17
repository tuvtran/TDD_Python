from django.test import TestCase

# Create your tests here.


class HomePageTest(TestCase):

    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        # Instead of checking the html's content
        # we now check if home_page() function
        # returns the right template which is home.html
        self.assertTemplateUsed(response, 'home.html')
