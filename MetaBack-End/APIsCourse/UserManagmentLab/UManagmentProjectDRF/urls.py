from django.urls import path
from . import views
urlpatterns = [
     path('rating',views.RatingView.as_view()),
]