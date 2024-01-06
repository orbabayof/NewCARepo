from .models import AuthorModel,BookStoreModel
from rest_framework import serializers

class AuthorModelSerializer(serializers.ModelSerializer):
     class Meta:
          model = AuthorModel
          fields = ['id','name','books_by_him']
class BookStoreModelSerializer(serializers.HyperlinkedModelSerializer):
     #author = AuthorModelSerializer
     class Meta:
          model = BookStoreModel
          fields = ['title','author','price']
         