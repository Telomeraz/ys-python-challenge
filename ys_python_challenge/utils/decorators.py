from pub_sub.pub import publish_data


def pub_data(func):
    def wrapper(obj, *args, **kwargs):
        response = func(obj, *args, **kwargs)

        publish_data(response.channel_name, response.to_dict())

        return response

    return wrapper
