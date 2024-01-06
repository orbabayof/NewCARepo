from .models import MenuItemsModel
from rest_framework import serializers
from decimal import Decimal
class MenuItemsModelSerializer(serializers.ModelSerializer):
     def calculateTax(self,product:MenuItemsModel):
          return product.price * Decimal(1.1)
     priceAfterTax = serializers.SerializerMethodField(method_name='calculateTax')
     class Meta:
          model = MenuItemsModel
          fields = ['id','title','price','inventory','priceAfterTax']