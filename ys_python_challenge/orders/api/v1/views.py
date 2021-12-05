from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from .serializers import OrderCreateSerializer, OrderListSerializer
from orders.exceptions import OrderAlreadyCompleted
from orders.models import Order
from utils.mixins import SerializerMixin


class OrderViewSet(SerializerMixin, CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = {
        "create": OrderCreateSerializer,
        "list": OrderListSerializer,
    }
    queryset = Order.objects.all()
    filterset_fields = ("status",)

    def get_queryset(self):
        return self.queryset.filter_owner(self.request.user)


@api_view(("POST",))
@permission_classes(())
def complete_order(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    try:
        order.do_complete()
    except OrderAlreadyCompleted:
        return Response(status=status.HTTP_409_CONFLICT)

    return Response(status=status.HTTP_204_NO_CONTENT)
