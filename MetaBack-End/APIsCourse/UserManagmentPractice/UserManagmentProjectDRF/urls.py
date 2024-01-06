from django.urls import path
from . import views
from .views import StoreItemView
urlpatterns = [
     path('store-items',StoreItemView.as_view()),
     path('make-manager',views.managers)
]