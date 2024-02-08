from django.shortcuts import render
from rest_framework import generics
from .models import Rating
from .serializers import RatingSerializer
from rest_framework import permissions
from rest_framework.throttling import UserRateThrottle
class RatingView(generics.ListCreateAPIView):
     permission_classes = [permissions.IsAuthenticated]
     queryset = Rating.objects.all()
     serializer_class = RatingSerializer
     throttle_classes = [UserRateThrottle]