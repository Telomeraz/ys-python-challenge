from django.db import models
from django.utils.translation import gettext_lazy as _

from .order_item import OrderItem


class OrderManager(models.Manager):
    def create(self, order_dict):
        items = order_dict.pop("items")

        order = self.model(**order_dict)
        order.save()

        self.create_items(items, order)

        return order

    def create_items(self, items, order):
        for item in items:
            item["order"] = order
            OrderItem.objects.create(item)


class Order(models.Model):
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
