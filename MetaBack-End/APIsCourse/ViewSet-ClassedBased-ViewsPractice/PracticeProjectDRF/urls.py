from django.urls import path
from .views import BooksViews

urlpatterns = [
     path('books/',BooksViews.as_view(
          {
               'get':'list',
               'post':'create',
          })
     ),
     path('books/<int:pk>',BooksViews.as_view(
          {
               'get':'retrive',
               'put' : 'update',
               'patch':'partial_update',
               'delete': 'destroy'
          }
     ))
]