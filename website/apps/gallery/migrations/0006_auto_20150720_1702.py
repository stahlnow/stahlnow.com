# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_image_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='gallery',
            field=models.ForeignKey(related_name='images', blank=True, to='gallery.Gallery', null=True),
            preserve_default=True,
        ),
    ]
