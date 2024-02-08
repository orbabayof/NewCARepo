from django.shortcuts import render
from .serializers import MenuItemSerializer
from . import models
from rest_framework import generics
# Create your views here.
class MenuItemView(generics.ListCreateAPIView):
     queryset = models.MenuItem.objects.all()
     serializer_class = MenuItemSerializer