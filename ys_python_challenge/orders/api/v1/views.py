from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .serializers import OrderCreateSerializer
from utils.mixins import SerializerMixin


class OrderViewSet(SerializerMixin, CreateModelMixin, GenericViewSet):
    serializer_class = {
        "create": OrderCreateSerializer,
    }
