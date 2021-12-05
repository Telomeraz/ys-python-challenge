from orders.exceptions import OrderAlreadyCompleted
from utils.base_test import BaseTest


class OrderTest(BaseTest):
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
