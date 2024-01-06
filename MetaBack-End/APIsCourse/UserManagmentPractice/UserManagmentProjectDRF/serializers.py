from .models import StoreItem
from rest_framework import serializers

class StoreItemSerializer(serializers.ModelSerializer):
     class Meta:
          model = StoreItem
          fields = ['id','title','price']