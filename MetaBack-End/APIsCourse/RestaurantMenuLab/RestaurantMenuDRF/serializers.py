from .models import MenuItemsModel
from rest_framework import serializers

class MenuItemsModelSerializer(serializers.ModelSerializer):
     class Meta:
        model = MenuItemsModel
        fields = ['id','title','price','inventory']
        extra_kwargs = {'price':{'min_value':2},'inventory':{'min_value':0}}