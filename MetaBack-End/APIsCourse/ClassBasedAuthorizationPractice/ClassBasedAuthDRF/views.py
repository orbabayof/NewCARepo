from django.shortcuts import render
from .serializers import ComputerStoreModelSerializer
from .models import ComputerStoreModel
from rest_framework import permissions,generics
from rest_framework.authentication import TokenAuthentication
from .perms import PermsForComputerStoreView,PermsForComputerStoreViewById
# Create your views here.

class ComputerStoreView(generics.ListCreateAPIView):
     queryset = ComputerStoreModel.objects.all()
     serializer_class = ComputerStoreModelSerializer
     authentication_classes = [TokenAuthentication]
     permission_classes = [permissions.IsAuthenticated,PermsForComputerStoreView]

class ComputerStoreViewById(generics.RetrieveUpdateDestroyAPIView):
     queryset = ComputerStoreModel.objects.all()
     authentication_classes = [TokenAuthentication]
     serializer_class = ComputerStoreModelSerializer
     permission_classes = [permissions.IsAuthenticated,PermsForComputerStoreViewById]