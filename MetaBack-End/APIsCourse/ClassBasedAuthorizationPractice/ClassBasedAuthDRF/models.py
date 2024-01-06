from django.db import models

# Create your models here.
class ComputerStoreModel(models.Model):
     name = models.CharField(max_length=255)
     price = models.SmallIntegerField()
     year = models.DateField()