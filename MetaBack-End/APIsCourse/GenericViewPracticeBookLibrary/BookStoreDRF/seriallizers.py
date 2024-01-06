from rest_framework import serializers
from .models import BookStoreModel

class BookStoreModelSeriallizer(serializers.ModelSerializer):
     class Meta:
          model = BookStoreModel
          fields = ['id','title','author','price','inventory']