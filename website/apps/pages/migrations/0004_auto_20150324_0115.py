# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_page_script'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='script',
            field=models.TextField(verbose_name='script', blank=True),
            preserve_default=True,
        ),
    ]
