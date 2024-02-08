from django.shortcuts import render
from .serializers import MenuSerializers
from . import models
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class MenuView(generics.ListCreateAPIView):
     queryset = models.Menu.objects.all()
     serializer_class = MenuSerializers


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
     queryset = models.Menu.objects.all()
     serializer_class = MenuSerializers
     permission_classes = [IsAuthenticated]