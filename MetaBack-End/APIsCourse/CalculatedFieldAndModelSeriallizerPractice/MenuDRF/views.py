from django.shortcuts import render
from .serializers import MenuItemsModelSerializer
from .models import MenuItemsModel
from rest_framework import generics
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer
class MenuItemsByIdView(generics.RetrieveUpdateDestroyAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer