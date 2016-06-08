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

from filer.fields.image import FilerImageField

class Image(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
    image = FilerImageField(blank=True, null=True)
    caption = models.TextField(_('caption'), blank=True, null=True)
    link = models.URLField(_('link'), blank=True, null=True)

    gallery = models.ForeignKey('Gallery', related_name='images', null=True, blank=True)

    class Meta:
        verbose_name = _('image')
        verbose_name_plural = _('images')
        db_table = 'gallery_images'
        ordering = ('-created',)
        get_latest_by = 'created'

    def __unicode__(self):
        return self.image.file.name


    def image_tag(self):
        return u'<img src="%s" width="400px" />' % (settings.FILES_URL + self.image.file.name)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

class Gallery(models.Model):
    uuid = UUIDField()
    created = CreationDateTimeField()
    updated = ModificationDateTimeField()
    name = models.CharField(max_length=1024)

    class Meta:
        verbose_name = _('gallery')
        verbose_name_plural = _('galleries')
        db_table = 'gallery_galleries'
        ordering = ('-created',)

    def __unicode__(self):
        return self.name

    @property
    def images(self):
        if self.images.exists():
            return self.images.all()