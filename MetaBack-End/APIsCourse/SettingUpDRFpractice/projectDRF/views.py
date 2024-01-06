from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIViewq
# Create your views here.
@api_view(['GET','POST'])
def HomeView(request):
     return Response("Welcome to Or's first DRF build",status=status.HTTP_200_OK)