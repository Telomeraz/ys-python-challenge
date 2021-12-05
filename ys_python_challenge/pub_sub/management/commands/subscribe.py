from django.core.management.base import BaseCommand

from pub_sub.sub import subscribe_data


class Command(BaseCommand):
    help = "To be notified of created orders"

    def handle(self, *args, **options):
        subscribe_data()
