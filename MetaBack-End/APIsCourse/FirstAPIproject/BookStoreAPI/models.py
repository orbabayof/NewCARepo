from django.db import models

# Create your models here.
class BookModel(models.Model):
     total = models.CharField(max_length=255)
     author = models.CharField(max_length=255)
     price = models.DecimalField(max_digits=5,decimal_places=2)
     inventory = models.SmallIntegerField()
     class Meta:
          models.Index(fields=['price'])
     