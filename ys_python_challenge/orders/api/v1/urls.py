from django.urls import path

from .views import OrderViewSet, complete_order


urlpatterns = [
    path(
        "order/create/",
        OrderViewSet.as_view({"post": "create"}),
        name="order-create",
    ),
    path(
        "order/<int:order_id>/complete/",
        complete_order,
        name="order-complete",
    ),
    path(
        "order/list/",
        OrderViewSet.as_view({"get": "list"}),
        name="order-list",
    ),
]
