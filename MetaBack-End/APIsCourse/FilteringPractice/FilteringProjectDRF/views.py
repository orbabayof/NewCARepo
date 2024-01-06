from django.shortcuts import render
from rest_framework import generics
from .models import MenuItemsModel
from .serializers import MenuItemsModelSerializer
# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer
     ordering_fields=['price','stock'] 
     search_fields=['title']