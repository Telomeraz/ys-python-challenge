from orders.exceptions import OrderAlreadyCompleted
from utils.base_test import BaseTest

from orders.models import Order, OrderItem


class OrderTest(BaseTest):
    def test_create(self):
        address = "18837 Reilly Gateway Apt. 894"
        order_items = [{"product": self.product, "unit_price": 40, "quantity": 5}]
        order_dict = {
            "owner": self.user,
            "address": address,
            "restaurant": self.restaurant,
            "items": order_items,
        }
        order = Order.objects.create(order_dict)
        order.refresh_from_db()

        self.assertEqual(order.owner.id, self.user.id)
        self.assertEqual(order.address, address)
        self.assertEqual(order.restaurant.id, self.restaurant.id)
        self.assertEqual(order.items.count(), len(order_items))

    def test_do_complete_if_status_is_pending(self):
        self.order.do_complete()
        self.assertEqual(self.order.status, self.order.Status.COMPLETED)

    def test_do_complete_if_status_is_completed(self):
        self.order.status = self.order.Status.COMPLETED
        self.assertRaises(OrderAlreadyCompleted, self.order.do_complete)

    def test_validate_can_complete_if_status_is_pending(self):
        self.order.status = self.order.Status.PENDING
        self.order.validate_can_complete()

    def test_validate_can_complete_if_status_is_completed(self):
        self.order.status = self.order.Status.COMPLETED
        self.assertRaises(OrderAlreadyCompleted, self.order.validate_can_complete)


class OrderItemTest(BaseTest):
    def test_create(self):
        order_item_dict = {
            "product": self.product,
            "unit_price": 40,
            "quantity": 5,
            "order": self.order,
        }
        order_item = OrderItem.objects.create(order_item_dict)
        order_item.refresh_from_db()

        self.assertEqual(order_item.product.id, self.product.id)
        self.assertEqual(order_item.unit_price, 40)
        self.assertEqual(order_item.quantity, 5)
        self.assertEqual(order_item.order.id, self.order.id)
