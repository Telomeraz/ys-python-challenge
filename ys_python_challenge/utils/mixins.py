class SerializerMixin:
    """
    Mixin class that helps with ViewSets which have dynamic serializer
    classes.
    """

    def get_serializer_class(self):
        return self.serializer_class[self.action]
