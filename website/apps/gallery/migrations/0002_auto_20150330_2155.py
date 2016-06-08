# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.TextField(null=True, verbose_name='caption', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='image',
            name='link',
            field=models.URLField(null=True, verbose_name='link', blank=True),
            preserve_default=True,
        ),
    ]
