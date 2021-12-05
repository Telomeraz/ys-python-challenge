import json
from redis import StrictRedis

from django.conf import settings


redis_client = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1)


def publish_data(channel_name, json_data):
    redis_client.publish(channel_name, json.dumps(json_data))
