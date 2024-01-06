from django.shortcuts import render
from rest_framework import generics
from .serializers import glassStoreSerializer
from .models import glassStore
from rest_framework import permissions 
# Create your views here.
class glassStoreView(generics.ListCreateAPIView):
     queryset = glassStore.objects.all()
     serializer_class = glassStoreSerializer
     permission_classes = [permissions.IsAuthenticated]