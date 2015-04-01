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

from fileupload.image import pillow_backend as backend

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
    tags = TaggableManager(blank=True)

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
        if (is_image(self.file.url)):
            return u'<img src="%s" />' % (self.file.url)
        elif (is_movie(self.file.url)):
            return u'<video autoplay loop muted src="%s" />' % (self.file.url)

    def file_tag_thumb(self):
        if (is_image(self.file.url)):
            if os.path.isfile(unicode('{0}_thumb{1}').format(*os.path.splitext(self.file.url))):
                return u'<a href="%s"><img src="%s" /></a>' % (self.pk, unicode('{0}_thumb{1}').format(*os.path.splitext(self.file.url)))
            else:
                return u'<a href="%s"><img src="%s" width=150px /></a>' % (self.pk, self.file.url)
        elif (is_movie(self.file.url)):
            return u'<a href="%s"><video width="300px" autoplay loop muted src="%s" /></a>' % (self.pk, self.file.url)

    file_tag.short_description = 'Content'
    file_tag.allow_tags = True
    file_tag_thumb.short_description = 'Preview'
    file_tag_thumb.allow_tags = True


def is_image(path):
    ext = path.split('.')[-1].lower()
    return ext in ['jpg', 'jpeg', 'png', 'gif', 'svg']

def is_movie(path):
    ext = path.split('.')[-1].lower()
    return ext in ['mp4', 'webm']

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

@receiver(models.signals.post_save, sender=File)
def generate_thumbnail(sender, instance, **kwargs):
    if instance.file:
        if os.path.isfile(instance.file.path):
            if backend.should_create_thumbnail(instance.file.path):
                backend.create_thumbnail(instance.file.path)
