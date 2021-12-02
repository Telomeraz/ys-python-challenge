from django.db import models
from django.utils.translation import gettext_lazy as _


class Restaurant(models.Model):
    """Represents the restaurant that the users can buy."""

    name = models.CharField(
        _("The display name of the restaurant"),
        max_length=255,
    )
