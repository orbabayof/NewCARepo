from django.urls import path
from .views import BooingSeralizerView,UserView
urlpatterns = [
     path('Booking/',BooingSeralizerView.as_view()),
     path('',UserView.as_view())
]