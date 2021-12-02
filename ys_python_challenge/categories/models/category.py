from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Represents category of products."""

    name = models.CharField(
        _("The display name of the category"),
        max_length=255,
    )
