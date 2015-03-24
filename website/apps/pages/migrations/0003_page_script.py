# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_remove_page_script'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='script',
            field=models.TextField(null=True, verbose_name='script'),
            preserve_default=True,
        ),
    ]
