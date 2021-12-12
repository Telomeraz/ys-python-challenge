from rest_framework import status

from django.urls import reverse

from utils.base_test import BaseTest


class OrderTest(BaseTest):
    def test_order_create_view_login_required(self):
        response = self.client.post(
            reverse("order-create"),
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_list_view_login_required(self):
        response = self.client.get(
            reverse("order-list"),
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_order_create_view(self):
        data = {
            "address": "2377 Twin Willow Lane Jacksonville NC North Carolina",
            "restaurant": 1,
            "items": [{"unit_price": 5, "quantity": 1}],
        }
        response = self.client.post(
            reverse("order-create"),
            data,
            **self.auth_headers,
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_order_complete_view(self):
        response = self.client.post(
            reverse("order-complete", kwargs={"order_id": 1}),
            **self.auth_headers,
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_order_list_view(self):
        response = self.client.get(
            reverse("order-list"),
            **self.auth_headers,
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
