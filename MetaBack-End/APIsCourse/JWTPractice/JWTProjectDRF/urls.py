from django.urls import path
from .views import glassStoreView
urlpatterns = [
     path('glass',glassStoreView.as_view())
]