from .models import SecretMessageModel
from rest_framework import serializers

class SecretMessageModelSerializer(serializers.ModelSerializer):
     class Meta:
          model = SecretMessageModel
          fields = ['id','sender','title','content']
