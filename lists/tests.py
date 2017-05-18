from django.test import TestCase

# Create your tests here.


class HomePageTest(TestCase):

    def test_uses_home_tempate(self):
        response = self.client.get('/')
        # Instead of checking the html's content
        # we now check if home_page() function
        # returns the right template which is home.html
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode('utf-8'))
        self.assertTemplateUsed(response, 'home.html')
