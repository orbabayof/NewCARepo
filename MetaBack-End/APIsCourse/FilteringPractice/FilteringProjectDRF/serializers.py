from rest_framework import serializers
from .models import MenuItemsModel

class MenuItemsModelSerializer(serializers.ModelSerializer):
     class Meta:
          model = MenuItemsModel
          fields = ['title','price','stock']