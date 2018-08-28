from django.shortcuts import render
from rest_framework import generics
from api.models import Restaurant, Order, Announcement, Table, Reservation
from api.serializers import RestaurantSerializer, OrderSerializer, AnnouncementSerializer, TableSerializer, ReservationSerializer


# Create your views here.
class AnnouncementListView(generics.ListAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TableListView(generics.ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationCreateView(generics.CreateAPIView):
    serializer_class = ReservationSerializer