import json
from redis import StrictRedis
import requests

from django.conf import settings

from orders.models import Order


def subscribe_data():
    """Listen and take action when published data.

    Note:
        It would be better if it was dynamic and reusable but i don't have
        knowledge of micro-service and pub/sub.
    """
    r = StrictRedis(host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=1)
    p = r.pubsub()
    p.psubscribe(Order.channel_name)
    for message in p.listen():
        if message:
            data = message.get("data", 1)
            if data != 1:
                data = json.loads(data)
                requests.post("http://127.0.0.1:8000/api/v1/orders/order/%s/complete/" % data["id"])
