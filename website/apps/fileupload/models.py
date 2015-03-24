# encoding: utf-8
import os
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django_extensions.db.fields import *

from taggit.managers import TaggableManager

file_store = FileSystemStorage(
    location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL)


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
