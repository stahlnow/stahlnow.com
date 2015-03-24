# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20150324_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='script',
            field=models.TextField(null=True, verbose_name='script', blank=True),
            preserve_default=True,
        ),
    ]
