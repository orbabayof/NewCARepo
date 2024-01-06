from django.urls import path
from .views import MenuItemsView,MenuItemsByIdView

urlpatterns = [
     path('menu-items',MenuItemsView.as_view()),
     path('menu-items/<int:pk>',MenuItemsByIdView.as_view())
]