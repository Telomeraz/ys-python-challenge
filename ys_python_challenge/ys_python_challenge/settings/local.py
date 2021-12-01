from decouple import config

from .base import *


SECRET_KEY = config("SECRET_KEY")

ALLOWED_HOSTS += ["*"]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": config("DB_NAME"),
    }
}
