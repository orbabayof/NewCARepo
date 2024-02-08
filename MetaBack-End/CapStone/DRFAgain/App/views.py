from django.shortcuts import render

# Create your views here.
from .serializers import BookingSerializer,UserSerializer
from django.contrib.auth.models import User
from .models import Booking
from rest_framework import generics
class BooingSeralizerView(generics.ListCreateAPIView):
     queryset = Booking.objects.all()
     serializer_class = BookingSerializer
class UserView(generics.ListCreateAPIView):
     queryset = User.objects.all()
     serializer_class = UserSerializer