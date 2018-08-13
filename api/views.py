from django.shortcuts import render
from rest_framework import generics
from api.models import Restaurant, Order
from api.serializers import RestaurantSerializer, OrderSerializer


# Create your views here.
class RestaurantListView(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer