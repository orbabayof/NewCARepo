from django.db import models

# Create your models here.
class AuthorModel(models.Model):
     name = models.CharField(max_length=100,default='donald')
     books_by_him = models.CharField(max_length=255,default='The carizma myth')
     def __str__(self) -> str:
          return self.name
class BookStoreModel(models.Model):
     title = models.CharField(max_length=255)
     author = models.ForeignKey(AuthorModel,on_delete=models.PROTECT)
     price = models.DecimalField(decimal_places=2,max_digits=6)