from rest_framework import serializers
from .models import glassStore

class glassStoreSerializer(serializers.ModelSerializer):
     class Meta:
          model = glassStore
          fields = ['id','brand','price']