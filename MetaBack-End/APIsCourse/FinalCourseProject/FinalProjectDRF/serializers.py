from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
     class Meta:
          model = models.Category
          fields = ['id','title','slug']    


class MenuItemSerializer(serializers.ModelSerializer):
     class Meta:
          model = models.MenuItem
          fields = ['id','title','price','featured','category']

class CartSerializer(serializers.ModelSerializer):
     user = serializers.PrimaryKeyRelatedField(
          queryset = User.objects.all(),
          default = serializers.CurrentUserDefault()
     )
     price = serializers.DecimalField(max_digits=6,decimal_places=2,read_only=True)
     class Meta:
          model = models.Cart
          fields = ['id','user','menuitem','quantity','unit_price','price']

class OrderSerializer(serializers.ModelSerializer):
     user = serializers.PrimaryKeyRelatedField(
          queryset = User.objects.all(),
          default = serializers.CurrentUserDefault()
     )
     total = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)  # Make total read-only
     class Meta:
          model = models.Order
          fields = ['id','user','delivery_crew','status','total','date']


#class OrderByIdSerializer(serializers.ModelSerializer):
#     class Meta:
#          model = models.OrderItem
#          fields = ['id','order','menuitem','quantity','unit_price','price']
#     def parial_update(self, instance, validated_data):
#        # Allow partial updates for the 'status' field only
#        if self.request.user.groups.filter(name='manager').exists():
#          instance.save()
#        else:
#            instance.status = validated_data.get('status', instance.status)
#            instance.save()
#        return instance

          