from .views import MenuItemsView,MenuItemsByIdView
from django.urls import path

urlpatterns = [
     path('menu-items',MenuItemsView.as_view()),
     path('menu-items/<int:pk>',MenuItemsByIdView.as_view())
]