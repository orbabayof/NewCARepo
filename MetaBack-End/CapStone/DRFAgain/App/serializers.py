from rest_framework.serializers import ModelSerializer
from .models import Booking
from django.contrib.auth.models import User
class UserSerializer(ModelSerializer):
     class Meta:
          model = User
          fields = ['username','email','groups']
class BookingSerializer(ModelSerializer):
     class Meta:
          model = Booking
          fields = ['id','BooingNo','Name']
