from django.shortcuts import render
from .models import MenuItemsModel
from .serializers import MenuItemsModelSerializer
from rest_framework import generics
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer
class MenuItemsByIdView(generics.RetrieveUpdateDestroyAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer