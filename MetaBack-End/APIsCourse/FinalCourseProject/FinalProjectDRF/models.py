from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
     slug = models.SlugField()
     title = models.CharField(max_length=255, db_index=True)
     def __str__(self) -> str:
          return self.title

class MenuItem(models.Model):
     title = models.CharField(max_length=255, db_index=True)
     price = models.DecimalField(decimal_places=2,max_digits=6,db_index=True)
     featured = models.BooleanField(db_index=True)
     category = models.ForeignKey(Category,on_delete=models.PROTECT)

     def __str__(self) -> str:
          return self.title

class Cart(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     menuitem = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
     quantity = models.IntegerField()
     unit_price = models.DecimalField(max_digits=6,decimal_places=2)
     price = models.DecimalField(max_digits=6,decimal_places=2)

     class Meta:
          unique_together = ('menuitem','user')

     def save(self, *args, **kwargs):
        # Calculate price before saving the object
        self.price = self.unit_price * self.quantity
        super(Cart, self).save(*args, **kwargs)
     
          
class Order(models.Model):
     user = models.ForeignKey(User,on_delete=models.CASCADE)
     delivery_crew = models.ForeignKey(User,on_delete=models.SET_NULL, related_name='delivery_crew',null=True)
     status = models.BooleanField(db_index=True,default=0)
     total = models.DecimalField(max_digits=6,decimal_places=2)
     date = models.DateField(db_index=True)

     

class OrderItem(models.Model):
     order = models.ForeignKey(Order,on_delete=models.CASCADE)
     menuitem = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
     quantity = models.SmallIntegerField()
     unit_price = models.DecimalField(max_digits=6,decimal_places=2)
     price = models.DecimalField(max_digits=6,decimal_places=2)

     