from rest_framework import permissions
from rest_framework.permissions import IsAdminUser

class AuthDeliveryCrewPerms(permissions.BasePermission):
     def has_permission(self, request, view):
          return request.user.groups.filter(name='manager').exists()
     
class AuthManagerPerms(permissions.BasePermission):
     def has_permission(self, request, view):
         return request.user.groups.filter(name='manager').exists() or IsAdminUser

class MenuItemViewPerms(permissions.BasePermission):
     def has_permission(self, request, view):
          if request.method == 'GET':
               return True
          return request.user.groups.filter(name='manager').exists() or IsAdminUser

class OrderViewGETPerms(permissions.BasePermission):
     def has_permission(self, request, view):
         return request.user.groups.filter(name='manager').exists() or IsAdminUser

class OrderItemPerms(permissions.BasePermission):
     def has_permission(self, request, view):
          if request.method == 'GET':
               return True
          if request.method == 'PATCH':
               return request.user.groups.filter(name='manager').exists() or request.user.groups.filter(name='delivery').exists()
          if request.method in ['DELETE', 'PUT']:
               return request.user.groups.filter(name='manager').exists() 