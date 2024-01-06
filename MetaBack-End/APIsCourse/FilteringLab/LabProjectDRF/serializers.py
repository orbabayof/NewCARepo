from rest_framework import serializers
from .models import MenuItemsModel,CatergoryModel

class CatergoryModelSerializer(serializers.ModelSerializer):
     class Meta:
          model = CatergoryModel
          fields = ['id','title']

class MenuItemsModelSerializer(serializers.ModelSerializer):
     #category = CatergoryModelSerializer
     class Meta:
          model = MenuItemsModel
          fields = ['id','title','price','inventory','catergory']
     