# YS Python Challenge

YS Python Challenge is an API that enables users can create, update and list order.

# Endpoints

* **/api/v1/orders/order/create/** Create API
* **/api/v1/orders/order/{order_id}/complete/** Complete API
* **/api/v1/orders/order/list/** List API

# Capabilities

* You can create an order via Order Create API. Order status will be PENDING by default. If you wish to be notified when a new order is created, you can subscribe (pub/sub) by typing:
```console
$ redis-cli
127.0.0.1:6379> PSUBSCRIBE orders
```

* After a new order is created, it will complete the order using Order Complete API or you can manually use the endpoint.
* In the end, you can list the orders.

For more detail about API, visit [Swagger Docs](http://127.0.0.1:8000/swagger/) and [ReDoc Docs](http://127.0.0.1:8000/redoc/).

[Contribution guidelines for this project](CONTRIBUTING.md)
