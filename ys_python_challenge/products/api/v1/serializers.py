from rest_framework import serializers

from categories.api.v1.serializers import CategoryListSerializer
from products.models import Product


class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
        )
