from django.urls import path
from .views import BookStoreView,AuthorView

urlpatterns = [
     path('books/',BookStoreView.as_view()),
     path('author/<int:pk>', AuthorView.as_view(),name='authormodel-detail')
]