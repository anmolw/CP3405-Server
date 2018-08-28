from rest_framework import serializers
from api.models import Restaurant, MenuItem, Order, OrderedItem, Announcement, Table, Reservation
from django.core.validators import ValidationError


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ('title', 'description', 'created_at')


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'price')


class RestaurantSerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ('id', 'name', 'thumbnail', 'items')


class OrderedItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedItem
        fields = ('item', 'quantity')


class OrderSerializer(serializers.ModelSerializer):
    items = OrderedItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'restaurant', 'items', 'date_placed')

    def create(self, validated_data):
        ordered_items_data = validated_data.pop("items")
        order = Order.objects.create(**validated_data)
        for item_data in ordered_items_data:
            ordered_item = OrderedItem.objects.create(order=order, **item_data)
        return order


class TableSerializer(serializers.ModelSerializer):
    seats_available = serializers.SerializerMethodField()

    def get_seats_available(self, obj):
        return 4 - obj.reservation_set.count()

    class Meta:
        model = Table
        fields = ('id', 'seats_available')


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('table', )

    def create(self, validated_data):
        table = validated_data.pop("table")
        if table.reservation_set.count() < 4:
            reservation = Reservation(table=table)
            reservation.save()
        else:
            raise ValidationError("Max 4 reservations allowed")
        return reservation
