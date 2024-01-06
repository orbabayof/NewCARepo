from django.shortcuts import render
from .models import MenuItemsModel,CatergoryModel
from .serializers import MenuItemsModelSerializer,CatergoryModelSerializer
from rest_framework import generics
# Create your views here.


class CategoryView(generics.ListCreateAPIView):
     queryset = CatergoryModel.objects.all()
     serializer_class = CatergoryModelSerializer

class MenuItemsView(generics.ListCreateAPIView):
     queryset = MenuItemsModel.objects.all()
     serializer_class = MenuItemsModelSerializer
     search_fields = ['title','catergory__title']
     ordering_fields = ['price','inventory']
     filterset_fields = ['price', 'inventory']
