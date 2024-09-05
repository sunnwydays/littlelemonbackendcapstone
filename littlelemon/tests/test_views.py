from django.test import TestCase
from restaurant.models import Menu
import json

class MenuViewTest(TestCase):
    def setUp(self):
        #add 3 menu items
        Menu.objects.create(title="Oven-baked Chicken Breast", price=14.98, inventory=100)
        Menu.objects.create(title="Lean Ground Beef", price=12.98, inventory=100)
        Menu.objects.create(title="Spaghetti", price=8.98, inventory=100)
        self.menu = Menu.objects.get(title="Oven-baked Chicken Breast")
        self.menu2 = Menu.objects.get(title="Lean Ground Beef")
        self.menu3 = Menu.objects.get(title="Spaghetti")
        self.menu.save()
        self.menu2.save()
        self.menu3.save()

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, 200)
        # implicitly tests that the response is a JSON list
        # implicitly tests that the list has successfully added 3 objects
        response_without_id = [
            {'title': item['title'], 'price': item['price'], 'inventory': item['inventory']}
            for item in response.data
        ]
        expected_response = [
            {'title': 'Oven-baked Chicken Breast', 'price': 14.98, 'inventory': 100},
            {'title': 'Lean Ground Beef', 'price': 12.98, 'inventory': 100},
            {'title': 'Spaghetti', 'price': 8.98, 'inventory': 100}
        ]
        self.assertEqual(response_without_id, expected_response)

# run this test since python manage.py test isn't working
# python manage.py test littlelemon.tests.test_views