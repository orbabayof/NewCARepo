from django.db import models
# Create your models here.
class Booking(models.Model):
     BooingNo = models.IntegerField()
     Name = models.CharField(max_length = 50)