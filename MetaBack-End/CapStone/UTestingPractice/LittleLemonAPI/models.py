from django.db import models

# Create your models here.
class MenuItem(models.Model):
     title = models.CharField(max_length = 50)
     price = models.DecimalField(max_digits =6,decimal_places=2)
     inventory = models.IntegerField()

     def get_item(self):
          return f'{self.title} : {str(self.price)}'
     def __str__(self) -> str:
          return self.title + " : " + str(self.price)