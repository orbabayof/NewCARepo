from django.test import TestCase
from django.core import serializers
from LittleLemonAPI import models
"""
class MenuTest(TestCase):
     def test_to_get_item(self):
          item = models.MenuItem.objects.create(title = 'IceCream',price=80,inventory=100)
          self.assertEqual(str(item),"IceCream : 80")"""
class SerializationTestCase(TestCase):
    def setUp(self):
        # Create two items for testing
        self.item1 = models.MenuItem.objects.create(title='Item 1', price=9.99, inventory=10)
        self.item2 = models.MenuItem.objects.create(title='Item 2', price=14.99, inventory=5)

    def test_serialization(self):
        # Serialize the items
        serialized_item1 = serializers.serialize('json', [self.item1])
        serialized_item2 = serializers.serialize('json', [self.item2])

        # Assert that the serialization is correct
        expected_item1 = f'[{{"model": "LittleLemonAPI.menuitem", "pk": {self.item1.pk}, "fields": {{"title": "Item 1", "price": 9.99, "inventory": 10}}}}]'
        expected_item2 = f'[{{"model": "LittleLemonAPI.menuitem", "pk": {self.item2.pk}, "fields": {{"title": "Item 2", "price": 14.99, "inventory": 5}}}}]'
        self.assertEqual(serialized_item1, expected_item1)
        self.assertEqual(serialized_item2, expected_item2)