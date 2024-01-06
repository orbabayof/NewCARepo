from django.urls import path
from .views import ComputerStoreView, ComputerStoreViewById
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
     path('computers',ComputerStoreView.as_view()),
     path('computers/<int:pk>',ComputerStoreViewById.as_view()),
     path('api-token-auth/',obtain_auth_token),
]