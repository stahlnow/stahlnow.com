# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0005_auto_20150330_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, name=b'uuid', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('image', models.ForeignKey(blank=True, to='fileupload.File', null=True)),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'gallery_images',
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
                'get_latest_by': 'created',
            },
            bases=(models.Model,),
        ),
    ]
