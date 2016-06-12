from django.db.models import Manager
from django.utils.timezone import now


class PublicManager(Manager):
    """Returns published posts that are not in the future."""

    def published(self):
        return self.get_queryset().filter(status__gte=2, publish__lte=now())


    def get_next_project(self):
        return self.get_queryset().filter(my_order=2)