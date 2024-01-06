from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet
# Create your views here.
class BookView(APIView):
     def get(self,request,pk):
          author = request.GET.get('author')
          if(author):
               return Response({'message':'you are viewing book number ' + str(pk) + ' by ' + author},status.HTTP_200_OK)
          return Response({'message':'you are viewing book number ' + str(pk)},status.HTTP_200_OK)
     def put(self,request,pk):
         return Response({'title':request.data.get('title')},status.HTTP_200_OK)
     def post(self,request,pk):
          return Response({'title':request.data.get('title')},status.HTTP_200_OK)

