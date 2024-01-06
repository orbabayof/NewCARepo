from django.shortcuts import render
from .serializers import SecretMessageModelSerializer
from .models import SecretMessageModel
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import SAFE_METHODS
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from . import perm
# Create your views here.

class SecretMessageView(generics.ListCreateAPIView):
     queryset = SecretMessageModel.objects.all()
     serializer_class = SecretMessageModelSerializer
     permission_classes = [IsAuthenticated,perm.permissionForSecretMessageView]