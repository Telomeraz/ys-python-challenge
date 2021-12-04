from rest_framework import serializers

from orders.models import Order, OrderItem


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
