from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    """Represents products that can bought by the users."""

    name = models.CharField(
        _("The display name of the product"),
        max_length=255,
    )

    restaurant = models.ForeignKey(
        "restaurants.Restaurant",
        on_delete=models.CASCADE,
        related_name="products",
        verbose_name=_("The restorant of the product"),
    )

    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.PROTECT,
        related_name="products",
        verbose_name=_("The category of the product"),
    )
