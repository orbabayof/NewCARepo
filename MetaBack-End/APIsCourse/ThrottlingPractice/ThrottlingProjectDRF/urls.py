from django.urls import path
from .views import bottleStoreView
urlpatterns = [
     path('store',bottleStoreView.as_view())
]