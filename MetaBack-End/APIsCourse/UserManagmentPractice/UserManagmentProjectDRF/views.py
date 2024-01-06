from django.shortcuts import render
from .models import StoreItem
from .serializers import StoreItemSerializer
from rest_framework import generics,status
from .perms import StoreItemViewPermissionCheck
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth.models import User,Group
from django.shortcuts import get_object_or_404
# Create your views here.
class StoreItemView(generics.ListCreateAPIView):
     queryset = StoreItem.objects.all()
     serializer_class = StoreItemSerializer
     permission_classes = [IsAuthenticated,StoreItemViewPermissionCheck]

@api_view(['POST','DELETE'])
@permission_classes([IsAdminUser])
def managers(request):
     username = request.data['username']
     if username:
          user = get_object_or_404(User,username=username)
          managers = Group.objects.get(name='manager')
          if request.method == 'POST':
               managers.user_set.add(user)
          elif request.method == 'DELETE':
               managers.user_set.remove(user)
          return(Response({'message':'ok'},))
     return Response({'message':'error'},status.HTTP_400_BAD_REQUEST)
          