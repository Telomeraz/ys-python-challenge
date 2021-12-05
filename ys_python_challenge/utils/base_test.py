import base64

from django.contrib.auth import get_user_model
from django.test import TestCase

from categories.models import Category
from orders.models import Order
from products.models import Product
from restaurants.models import Restaurant


User = get_user_model()


class BaseTest(TestCase):
    @classmethod
    def setUpTestData(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.auth_headers = {
            "HTTP_AUTHORIZATION": "Basic "
            + base64.b64encode(
                f"{self.user.username}:{self.user.username}".encode(),
            ).decode("ascii"),
            "content_type": "application/json",
        }

        self.category = Category.objects.create(name="Döner/Kebap")
        self.restaurant = Restaurant.objects.create(name="Süper Dönerci")
        self.product = Product.objects.create(
            name="Döner",
            category=self.category,
            restaurant=self.restaurant,
            unit_price=30,
        )

        order_items = [{"product": self.product, "unit_price": 30, "quantity": 2}]
        order_dict = {
            "owner": self.user,
            "address": "246 Flanigan Oaks Drive Herndon MD Maryland",
            "restaurant": self.restaurant,
            "items": order_items,
        }
        self.order = Order.objects.create(order_dict)
