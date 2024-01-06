from django.shortcuts import render
from rest_framework import generics
from .models import BookStoreModel
from .seriallizers import BookStoreModelSeriallizer
# Create your views here.
class BookStoreView(generics.ListCreateAPIView):
     queryset = BookStoreModel.objects.all()
     serializer_class = BookStoreModelSeriallizer
class BookStoreByIdView(generics.RetrieveUpdateDestroyAPIView):
     queryset = BookStoreModel.objects.all()
     serializer_class = BookStoreModelSeriallizer