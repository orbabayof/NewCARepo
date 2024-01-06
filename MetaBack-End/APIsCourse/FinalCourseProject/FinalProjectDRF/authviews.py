from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from django.contrib.auth.models import User,Group
from rest_framework import status
from django.shortcuts import get_object_or_404
from . import perms
from rest_framework.throttling import UserRateThrottle

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated,perms.AuthManagerPerms])
@throttle_classes([UserRateThrottle])
def ListCreateManagers(request):
     if request.method == 'GET':
        managers_group = Group.objects.get(name='manager')
        managers_users = managers_group.user_set.all()
        return Response({'managers': [user.username for user in managers_users]}, status=status.HTTP_200_OK)
     if request.method == 'POST':
       username = request.data['username']
       managers = Group.objects.get(name = 'manager')
       if username:
           user = get_object_or_404(User,username = username)
           managers.user_set.add(user)
           return Response({'messege': 'Manager Assigned!'})
       else:
           return Response({'messege':'error'},status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated,perms.AuthManagerPerms])
@throttle_classes([UserRateThrottle])
def DeleteManagersById(request,pk):
       managers = Group.objects.get(name = 'manager')
       user = get_object_or_404(User,pk = pk)
       if user.groups.filter(name='manager').exists():
          managers.user_set.remove(user)
          return Response({'messege': 'Manager Removed!'})
       else:
          return Response({'messege':'Error : This user is not in the manager group'},status.HTTP_404_NOT_FOUND)
       
@api_view(['POST','GET'])
#@permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated,perms.AuthDeliveryCrewPerms])
@throttle_classes([UserRateThrottle])
def ListCreateDeliveryCrew(request):
     if request.method == 'GET':
        delivery_group = Group.objects.get(name='delivery')
        delivery_users = delivery_group.user_set.all()
        return Response({'delivery_crew': [user.username for user in delivery_users]}, status=status.HTTP_200_OK)
     if request.method == 'POST':
       username = request.data['username']
       delivery = Group.objects.get(name = 'delivery')
       if username:
           user = get_object_or_404(User,username = username)
           delivery.user_set.add(user)
           return Response({'messege': 'Delivery Crew Assigned!'})
       else:
           return Response({'messege':'error'},status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
#@permission_classes([IsAdminUser])
@permission_classes([IsAuthenticated,perms.AuthDeliveryCrewPerms])
@throttle_classes([UserRateThrottle])
def DeleteDeleveryCrewById(request,pk):
       delivery = Group.objects.get(name = 'delivery')
       user = get_object_or_404(User,pk = pk)
       if user.groups.filter(name='delivery').exists():
          delivery.user_set.remove(user)
          return Response({'messege': 'Delivery crew member Removed!'})
       else:
          return Response({'messege':'Error : This user is not in the delivery group'},status.HTTP_404_NOT_FOUND)

