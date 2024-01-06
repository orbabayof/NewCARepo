from rest_framework import serializers
from .models import Rating
from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User

class RatingSerializer(serializers.ModelSerializer):
     user = serializers.PrimaryKeyRelatedField(
          queryset = User.objects.all(),
          default = serializers.CurrentUserDefault())
     def validate(self, attrs):
          if(attrs['menu_item_id']<1):
               raise serializers.ValidationError('invalid menu item id')
          if(attrs['rating']<0 or attrs['rating']>5):
               raise serializers.ValidationError('invalid rating, rating should be 0-5')
          return super().validate(attrs)
     
     class Meta:
     
          model = Rating
          fields = ['user','menu_item_id','rating']
          validators = [
               UniqueTogetherValidator(
                    queryset=Rating.objects.all(),
                    fields=['menu_item_id','rating']
               )
          ]