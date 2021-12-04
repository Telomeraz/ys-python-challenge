from django.urls import path

from .views import OrderViewSet


urlpatterns = [
    path(
        "order/create/",
        OrderViewSet.as_view({"post": "create"}),
        name="order-create",
    ),
]
