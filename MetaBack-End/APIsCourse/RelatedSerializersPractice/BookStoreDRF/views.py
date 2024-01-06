from django.shortcuts import render
from rest_framework import generics
from .models import BookStoreModel,AuthorModel
from .serializers import BookStoreModelSerializer,AuthorModelSerializer
# Create your views here.
class BookStoreView(generics.ListCreateAPIView):
     queryset = BookStoreModel.objects.all()
     serializer_class = BookStoreModelSerializer
class AuthorView(generics.RetrieveUpdateDestroyAPIView):
     queryset = AuthorModel
     serializer_class = AuthorModelSerializer