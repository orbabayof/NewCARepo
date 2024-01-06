from django.urls import path
from .views import SecretMessageView
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
     path('api-token-auth/',obtain_auth_token),
     path('secret-message',SecretMessageView.as_view())
]