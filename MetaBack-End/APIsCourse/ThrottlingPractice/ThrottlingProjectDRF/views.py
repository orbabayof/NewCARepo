from django.shortcuts import render
from .serializers import bottleStoreModelSerializer
from .models import bottleStoreModel
from rest_framework import generics
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class bottleStoreView(generics.ListCreateAPIView):
     def get_throttles(self):
          if self.request.method == 'POST':
               throttle_classes = [AnonRateThrottle]
          else:
               throttle_classes = [] 
          return [throttle() for throttle in throttle_classes]
     queryset = bottleStoreModel.objects.all()
     serializer_class = bottleStoreModelSerializer