from rest_framework import serializers
from .models import MenuItemsModel

class MenuItemsModelSeriallizer(serializers.ModelSerializer):
     class Meta:
        model = MenuItemsModel
        fields = ['id','title','price','inventory']
