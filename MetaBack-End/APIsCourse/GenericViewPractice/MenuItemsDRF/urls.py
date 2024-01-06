from .views import MenuItemsView,MenuItemsByIDView
from django.urls import path

urlpatterns = [
     path('menu-items',MenuItemsView.as_view()),
     path('menu-items/<int:pk>',MenuItemsByIDView.as_view()),
]