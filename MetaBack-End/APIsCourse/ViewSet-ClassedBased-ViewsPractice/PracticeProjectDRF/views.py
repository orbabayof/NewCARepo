from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class BooksViews(viewsets.ViewSet):
     #books/
     def list(self,request):
          return Response({'message':'all books'},status.HTTP_200_OK)
     def create(self,request):
          return Response({'message':'all books created'},status.HTTP_201_CREATED)
     #books/{booksId}
     def update(self,request,pk = None):
          return Response({'message':'book updated'},status.HTTP_200_OK)
     def retrive(self,request,pk = None):
          return Response({'message':'you see one book now '})
     def partial_update(self,request,pk = None):
          return Response({'message':'parially updated one book'},status.HTTP_200_OK)
     def destroy(self,request,pk = None):
          return Response({'message':'destroyed one book'},status.HTTP_200_OK)
     
     
