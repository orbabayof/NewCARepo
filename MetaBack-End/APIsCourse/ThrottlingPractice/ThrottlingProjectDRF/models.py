from django.db import models

# Create your models here.
class bottleStoreModel(models.Model):
     brand = models.CharField(max_length=255)
     price = models.CharField(max_length=255)