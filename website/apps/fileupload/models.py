# encoding: utf-8
import os
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django_extensions.db.fields import *

from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from taggit.managers import TaggableManager

file_store = FileSystemStorage(
    location=settings.FILES_ROOT, base_url=settings.FILES_URL)


def generate_file_path(obj, file):
    path = "%s%s" % (obj.uuid, os.path.splitext(file)[1])
    return path.replace('-', '/')


class File(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
    file = models.FileField(upload_to=generate_file_path, storage=file_store)
    tags = TaggableManager()

    class Meta:
        verbose_name = _('file')
        verbose_name_plural = _('files')
        db_table = 'fileupload_files'
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return self.file.name

    @models.permalink
    def get_absolute_url(self):
        return 'upload_new'

    def save(self, *args, **kwargs):
        super(File, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete(False)
        super(File, self).delete(*args, **kwargs)

    def file_tag(self):
        n, ext = os.path.splitext(self.file.name)
        if (ext == '.jpg' or ext == 'jpeg' or ext == 'gif' or ext == '.png'):
            return u'<img src="%s" width="400px" />' % (settings.FILES_URL + self.file.name)
        elif (ext == '.mp4' or ext == '.webm'):
            return u'<video autoplay loop muted src="%s" />' % (settings.FILES_URL + self.file.name)

    file_tag.short_description = 'File'
    file_tag.allow_tags = True


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