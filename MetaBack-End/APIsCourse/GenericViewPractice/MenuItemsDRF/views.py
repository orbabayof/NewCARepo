from django.shortcuts import render
from .models import MenuItemsModel
from .seriallizers import MenuItemsModelSeriallizer
from rest_framework import generics
from rest_framework import filters
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSeriallizer
     filter_backends = [filters.OrderingFilter]
     ordering_fields = ['price']
     

class MenuItemsByIDView(generics.RetrieveUpdateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSeriallizer
