# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_auto_20150720_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, name=b'uuid', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('name', models.CharField(max_length=1024)),
            ],
            options={
                'ordering': ('-created',),
                'db_table': 'gallery_galleries',
                'verbose_name': 'gallery',
                'verbose_name_plural': 'galleries',
            },
            bases=(models.Model,),
        ),
    ]
