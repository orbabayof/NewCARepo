from django.db import models

# Create your models here.
class SuperModel(models.Model):
     vegtables = models.CharField(max_length=255)
     meat = models.CharField(max_length=255)
     workers = models.IntegerField(default=5)