import json
from redis import StrictRedis

from django.conf import settings


redis_client = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1)


def publish_data(channel_name, data):
    """Publish data for subscribers.

    Args:
        channel_name (str)
        data (dict)
    """
    redis_client.publish(channel_name, json.dumps(data))
