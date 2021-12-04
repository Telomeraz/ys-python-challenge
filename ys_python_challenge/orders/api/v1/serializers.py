from rest_framework import serializers

from orders.models import Order, OrderItem
from products.api.v1.serializers import ProductListSerializer
from restaurants.api.v1.serializers import RestaurantListSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = (
            "product",
            "unit_price",
            "quantity",
        )


class OrderCreateSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = (
            "created_at",
            "address",
            "status",
            "restaurant",
            "items",
        )

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        instance = self.Meta.model.objects.create(order_dict=validated_data)
        return instance


class OrderItemListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = OrderItem
        fields = (
            "id",
            "product",
            "unit_price",
            "quantity",
        )


class OrderListSerializer(serializers.ModelSerializer):
    items = OrderItemListSerializer(many=True)

    restaurant = RestaurantListSerializer()

    class Meta:
        model = Order
        fields = (
            "id",
            "created_at",
            "address",
            "status",
            "restaurant",
            "items",
        )
