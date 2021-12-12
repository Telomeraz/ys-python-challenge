from django.core import validators
from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderItemManager(models.Manager):
    def create(self, order_item_dict):
        """Create new instance of :model:`orders.OrderItem`

        Args:
            order_item_dict (dic)

        Returns:
            obj of :model:`orders.OrderItem
        """
        order_item = self.model(**order_item_dict)
        order_item.save()
        return order_item


class OrderItem(models.Model):
    """Represents the item of its order."""

    order = models.ForeignKey(
        "orders.Order",
        on_delete=models.CASCADE,
        related_name="items",
        verbose_name=_("The order of the item"),
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.SET_NULL,
        null=True,
        related_name="order_items",
        verbose_name=_("The product of the item"),
    )

    unit_price = models.DecimalField(
        decimal_places=2,
        max_digits=12,
        validators=(validators.MinValueValidator(0),),
        verbose_name=_("The unit price of the item"),
    )

    quantity = models.PositiveSmallIntegerField(
        _("The quantity of the item"),
        validators=(validators.MinValueValidator(1),),
    )

    objects = OrderItemManager()
