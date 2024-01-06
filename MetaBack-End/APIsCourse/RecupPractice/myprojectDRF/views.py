from django.shortcuts import render
from .models import SuperModel
from .serializers import SuperModelSerializer
from rest_framework import generics
# Create your views here.
class SuperModelView(generics.ListCreateAPIView):
     queryset = SuperModel.objects.all()
     serializer_class = SuperModelSerializer

class SuperModelViewById(generics.RetrieveUpdateDestroyAPIView):
     queryset = SuperModel.objects.all()
     serializer_class = SuperModelSerializer