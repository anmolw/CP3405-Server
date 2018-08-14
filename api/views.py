from django.shortcuts import render
from rest_framework import generics
from api.models import Restaurant, Order, Announcement
from api.serializers import RestaurantSerializer, OrderSerializer, AnnouncementSerializer


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