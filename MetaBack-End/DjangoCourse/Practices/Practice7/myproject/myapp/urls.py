from django.urls import path
from .views import about,home,menu
urlpatterns = [
     path('',home),
     path('about/',about),
     path('menu/',menu)
]