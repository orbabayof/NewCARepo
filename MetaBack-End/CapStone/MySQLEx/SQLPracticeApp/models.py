from django.db import models

# Create your models here.
class BookStoreModel(models.Model):
     Name = models.CharField(max_length = 5)
     Price = models.IntegerField()