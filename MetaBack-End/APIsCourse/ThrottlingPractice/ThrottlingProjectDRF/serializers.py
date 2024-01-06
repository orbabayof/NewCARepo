from rest_framework import serializers
from .models import bottleStoreModel

class bottleStoreModelSerializer(serializers.ModelSerializer):
     class Meta:
          model = bottleStoreModel
          fields = ['id','brand','price']