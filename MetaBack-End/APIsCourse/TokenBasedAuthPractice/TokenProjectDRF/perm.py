from rest_framework import permissions

class permissionForSecretMessageView(permissions.BasePermission):
     def has_permission(self, request, view):
        # Allow 'GET', 'HEAD', and 'OPTIONS' requests for all users
            if request.method == 'GET':
                  
               return True
            if request.method == 'POST':
        # Allow 'POST' request only for users in 'manager' group
               return request.user.groups.filter(name='manager').exists()