from django.urls import path
from .views import SuperModelView, SuperModelViewById
urlpatterns = [
     path('super',SuperModelView.as_view()),
     path('super/<int:pk>',SuperModelViewById.as_view()),
]