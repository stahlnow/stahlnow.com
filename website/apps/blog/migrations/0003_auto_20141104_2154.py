# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=ckeditor.fields.RichTextField(verbose_name='body'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='tease',
            field=ckeditor.fields.RichTextField(help_text='Concise text suggested. Does not appear in RSS feed.', verbose_name='tease', blank=True),
            preserve_default=True,
        ),
    ]
