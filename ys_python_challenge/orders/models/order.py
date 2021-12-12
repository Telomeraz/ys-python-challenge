from django.db import models
from django.utils.translation import gettext_lazy as _

from .order_item import OrderItem
from ..exceptions import OrderAlreadyCompleted
from ..mixins import OrderChannelMixin
from utils.decorators import pub_data


class OrderQuerySet(models.QuerySet):
    def filter_owner(self, owner):
        """Filter by owner.

        Args:
            owner (obj of :model:`accounts.User)

        Returns:
            QuerySet
        """
        return self.filter(owner=owner)


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)

    @pub_data
    def create(self, order_dict):
        """Crete new instance of :model:`orders.Order` and its item objects.

        Args:
            order_dict (dict)

        Returns:
            obj of :model:`orders.Order`
        """
        items = order_dict.pop("items")

        order = self.model(**order_dict)
        order.save()

        order.create_items(items)

        return order


class Order(OrderChannelMixin, models.Model):
    """Represents the order that the users can give."""

    class Status(models.TextChoices):
        PENDING = "PENDING", _("Pending")
        COMPLETED = "COMPLETED", _("Completed")

    created_at = models.DateTimeField(
        _("The date and time that order was created"),
        auto_now_add=True,
    )

    address = models.TextField(_("The address of the order"))

    status = models.CharField(
        _("The status of the order"),
        choices=Status.choices,
        default=Status.PENDING,
        max_length=9,
    )

    owner = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("The owner of the order"),
    )

    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
        related_name="orders",
        verbose_name=_("The restorant of the order"),
    )

    objects = OrderManager()

    def do_complete(self):
        """Change status of order to COMPLETED"""
        self.validate_can_complete()
        self.status = self.Status.COMPLETED
        self.save()

    def validate_can_complete(self):
        """Check if order can be completed.

        Raises:
            OrderAlreadyCompleted: Raise when it's already completed.
        """
        if self.status == self.Status.COMPLETED:
            raise OrderAlreadyCompleted

    def create_items(self, items):
        """Create items of order.

        Args:
            items (list)
        """
        for item in items:
            item["order"] = self
            OrderItem.objects.create(item)
