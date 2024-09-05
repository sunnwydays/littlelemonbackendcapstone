from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        """
        Test the string representation of the Menu model
        First have to convert to string type
        """
        item = Menu.objects.create(title="Greek pasta", price=12.98, inventory=100)
        self.assertEqual(str(item), "Greek pasta : 12.98")

# run this test since python manage.py test isn't working
# python manage.py test littlelemon.tests.test_models