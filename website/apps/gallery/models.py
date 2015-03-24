# encoding: utf-8
import os
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django_extensions.db.fields import *

from django.db.models.signals import post_delete
from django.dispatch import receiver

from taggit.managers import TaggableManager

file_store = FileSystemStorage(
    location=settings.GALLERY_ROOT, base_url=settings.GALLERY_URL)


def generate_file_path(obj, file):
    path = "%s%s" % (obj.uuid, os.path.splitext(file)[1])
    return path.replace('-', '/')


class File(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
    file = models.FileField(upload_to=generate_file_path, storage=file_store)

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        db_table = 'gallery_files'
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return self.file.name


@receiver(models.signals.post_delete, sender=File)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding 'File' object is deleted.
    """
    if instance.file:
        if os.path.isfile(instance.file.path):
            os.remove(instance.file.path)

@receiver(models.signals.pre_save, sender=File)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding 'File' object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = File.objects.get(pk=instance.pk).file
    except File.DoesNotExist:
        return False

    new_file = instance.file
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

