from django.db.models import Manager
from django.utils import timezone


class PublicManager(Manager):
    """Returns published posts that are not in the future."""

    def published(self):
        #return self.get_queryset().filter(status__gte=2, publish__lte=timezone.now())
        return self.get_queryset().filter(status__gte=2)