from django.urls import path
from . import authviews
from . import views
urlpatterns = [
     path('groups/manager/users',authviews.ListCreateManagers),
     path('groups/manager/users/<int:pk>',authviews.DeleteManagersById),
     path('groups/delivery-crew/users',authviews.ListCreateDeliveryCrew),
     path('groups/delivery-crew/users/<int:pk>',authviews.DeleteDeleveryCrewById),
     path('category',views.CategoryView.as_view()),
     path('menu-items',views.MenuItemView.as_view()),
     path('menu-items/<int:pk>',views.MenuItemViewById.as_view()),
     path('cart/menu-items',views.CartView.as_view()),
     path('orders',views.OrderView.as_view()),
     path('orders/<int:pk>',views.OrderItemView.as_view())
]