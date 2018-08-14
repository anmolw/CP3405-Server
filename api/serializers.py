from rest_framework import serializers
from api.models import Restaurant, MenuItem, Order, OrderedItem, Announcement


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