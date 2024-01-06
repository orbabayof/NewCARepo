from rest_framework import serializers
from .models import ComputerStoreModel

class ComputerStoreModelSerializer(serializers.ModelSerializer):
     def validate(self, attrs):
          if attrs['price']<0:
               raise serializers.ValidationError('price cannot be negitive')
          return super().validate(attrs)
     class Meta:
          model = ComputerStoreModel
          fields = ['id','name','price','year']
