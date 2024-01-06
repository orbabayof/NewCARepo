from django.db import models

# Create your models here.
class formModel(models.Model):
     firstName = models.CharField(max_length=200)
     email = models.EmailField()