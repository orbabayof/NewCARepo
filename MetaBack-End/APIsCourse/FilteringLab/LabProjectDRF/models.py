from django.db import models

# Create your models here.
class CatergoryModel(models.Model):
     title = models.CharField(max_length=255)

     #def __str__(self) -> str:
      #    return self.title

class MenuItemsModel(models.Model):
     title = models.CharField(max_length=255)
     price = models.DecimalField(decimal_places=2,max_digits=6)
     inventory = models.SmallIntegerField()
     catergory = models.ForeignKey(CatergoryModel,on_delete=models.PROTECT)
