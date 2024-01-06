from django.shortcuts import render
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,action
from django.contrib.auth.models import User,Group
from . import serializers
from . import models
from . import perms
from rest_framework import generics,status
from rest_framework.exceptions import PermissionDenied
from rest_framework.views import APIView
from rest_framework.throttling import UserRateThrottle
# Create your views here.

class CategoryView(generics.ListCreateAPIView):
     queryset = models.Category.objects.all()
     serializer_class = serializers.CategorySerializer
     throttle_classes = [UserRateThrottle]

class MenuItemView(generics.ListCreateAPIView):
     queryset = models.MenuItem.objects.all()
     serializer_class = serializers.MenuItemSerializer
     permission_classes = [IsAuthenticated,perms.MenuItemViewPerms]
     throttle_classes = [UserRateThrottle]
     ordering_fields = ['price','title']
     filterset_fields = ['price','category','featured']
     search_fields = ['title','category']

class MenuItemViewById(generics.RetrieveUpdateDestroyAPIView):
     queryset = models.MenuItem.objects.all()
     serializer_class = serializers.MenuItemSerializer
     permission_classes = [IsAuthenticated,perms.MenuItemViewPerms]
     throttle_classes = [UserRateThrottle]

class CartView(generics.ListCreateAPIView,generics.DestroyAPIView):
     queryset = models.Cart.objects.all()
     serializer_class = serializers.CartSerializer
     permission_classes = [IsAuthenticated]
     throttle_classes = [UserRateThrottle]

     def get_queryset(self):
          user = self.request.user
          queryset = models.Cart.objects.filter(user=user)
          return queryset
     
     def perform_create(self, serializer):
          serializer.save(user=self.request.user)

     def delete(self, request, *args, **kwargs):
        # Handle DELETE request to delete user carts
        user = self.request.user
        models.Cart.objects.filter(user=user).delete()
        return Response({'messege':'cart deleted seccessfuly'})


class OrderView(generics.ListCreateAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated]
    ordering_fields = ['date','status','total']
    filterset_fields = ['status','total','user']
    search_fields = ['user']
    throttle_classes = [UserRateThrottle]

    def get_queryset(self):
        if self.request.user.groups.filter(name='manager').exists()== True or self.request.user.groups.filter(name='delivery').exists()== True:
            return models.Order.objects.all()
        else:
          user = self.request.user
          return models.Order.objects.filter(user=user)

    def perform_create(self, serializer):
        user = self.request.user

        # Calculate total price from user's cart items
        cart_items = models.Cart.objects.filter(user=user)
        total_price = sum(item.price for item in cart_items)
        
        order = serializer.save(user=user, total=total_price)
        for cart_item in cart_items:
            models.OrderItem.objects.create(
                order=order,
                menuitem=cart_item.menuitem,
                quantity=cart_item.quantity,
                unit_price=cart_item.unit_price,
                price=cart_item.price
            )
        # Create the Order object with the calculated total price

        cart_items.delete()

        return order
    


class OrderItemView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAuthenticated,perms.OrderItemPerms]
    queryset = models.Order.objects.all()
    throttle_classes = [UserRateThrottle]
    def get_queryset(self):
        if self.request.user.groups.filter(name='manager').exists()==True or self.request.user.groups.filter(name='delivery').exists()== True:
            return models.Order.objects.all()
        user = self.request.user
        return models.Order.objects.filter(user=user)
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Ensure that non-manager users can only update the 'status' field
        if not request.user.groups.filter(name='manager').exists():
            if 'status' in request.data and len(request.data.keys()) == 1:
                instance.status = request.data['status']
                instance.save()
                return Response(serializer.data)
            else:
                return Response({'error': 'You do not have permission to update this field.'}, status=status.HTTP_403_FORBIDDEN)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)