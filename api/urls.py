from django.urls import path
from api.views import RestaurantListView, OrderListCreateView

urlpatterns = [
    path('restaurants', RestaurantListView.as_view(), name="restaurants"),
    path('orders', OrderListCreateView.as_view(), name="orders")
]
