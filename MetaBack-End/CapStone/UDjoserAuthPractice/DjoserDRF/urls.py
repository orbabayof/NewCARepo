from django.urls import path
from .views import UserView
urlpatterns = [
     path('UserRegister/',UserView.as_view()),
]