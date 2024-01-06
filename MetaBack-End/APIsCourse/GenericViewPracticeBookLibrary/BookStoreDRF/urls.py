from django.urls import path
from . import views

urlpatterns = [
     path('books/',views.BookStoreView.as_view()),
     path('books/<int:pk>',views.BookStoreByIdView.as_view())
]