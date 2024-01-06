from django.db import models

# Create your models here.
class SecretMessageModel(models.Model):
     sender = models.CharField(max_length=255)
     title = models.CharField(max_length=255)
     content = models.TextField(max_length=2000)