from django.urls import path
from .views import menuByID
urlpatterns = [
     path('',menuByID)
]