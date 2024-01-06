from django.db import models

# Create your models here.
class Menu(models.Model):
     itemName = models.CharField(max_length=50)
     price = models.IntegerField()

     def __str__(self) -> str:
          return self.itemName