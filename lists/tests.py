from django.core.urlresolvers import resolve
from django.test import TestCase
from lists.views import home_page

# Create your tests here.


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # The idea is to test if resolve when called with "/"
        # finds a function called home_page
        found = resolve('/')
        self.assertEqual(found.func, home_page)
