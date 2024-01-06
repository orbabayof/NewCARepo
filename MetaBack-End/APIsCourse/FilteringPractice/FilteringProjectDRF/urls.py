from django.urls import path
from .views import MenuItemsView
urlpatterns = [
     path('menu-items',MenuItemsView.as_view())
]