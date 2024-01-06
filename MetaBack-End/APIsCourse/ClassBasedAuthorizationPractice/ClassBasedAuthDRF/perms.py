from rest_framework import permissions

class PermsForComputerStoreView(permissions.BasePermission):
     def has_permission(self, request, view):
          if request.method == 'GET':
               return True
          if request.method == 'POST':
               return request.user.groups.filter(name='manager').exists()
          
     
class PermsForComputerStoreViewById(permissions.BasePermission):
     def has_permission(self, request, view):
          if request.method == 'POST' or request.method == 'PATCH' or request.method == 'PUT':
               return request.user.groups.filter(name='manager').exists()
          else:
               return True