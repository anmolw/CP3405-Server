from django.urls import path
from api.views import RestaurantListView, OrderListCreateView, AnnouncementListView, TableListView, ReservationCreateView

urlpatterns = [
    path('announcements', AnnouncementListView.as_view(), name="announcements"),
    path('restaurants', RestaurantListView.as_view(), name="restaurants"),
    path('orders', OrderListCreateView.as_view(), name="orders"),
    path('tables', TableListView.as_view(), name="tables"),
    path('reservations', ReservationCreateView.as_view(), name="reservations")
]
