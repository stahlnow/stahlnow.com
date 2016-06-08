# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20150330_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
    ]
