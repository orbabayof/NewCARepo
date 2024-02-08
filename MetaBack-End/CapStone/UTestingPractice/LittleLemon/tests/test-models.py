from django.test import TestCase
from LittleLemonAPI import models
class MenuTest(TestCase):
     def test_to_get_item(self):
          item = models.MenuItem.objects.create(title = 'IceCream',price=80,inventory=100)
          self.assertEqual(item,"<MenuItem: IceCream : 80>")