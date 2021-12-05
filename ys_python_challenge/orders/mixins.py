from django.forms.models import model_to_dict


class OrderChannelMixin:
    channel_name = "orders"

    def to_dict(self):
        return model_to_dict(self)
