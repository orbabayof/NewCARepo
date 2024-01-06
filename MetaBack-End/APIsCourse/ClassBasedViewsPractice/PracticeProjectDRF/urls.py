from django.urls import path
from .views import BookView
urlpatterns = [
     path('books/<int:pk>',BookView.as_view())
]