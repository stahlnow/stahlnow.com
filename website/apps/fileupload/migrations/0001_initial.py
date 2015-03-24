# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django.core.files.storage
import django_extensions.db.fields
import fileupload.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid', django_extensions.db.fields.UUIDField(editable=False, name=b'uuid', blank=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('updated', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, editable=False, blank=True)),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/home/stahl/python/stahlnow/stahlnow/media'), upload_to=fileupload.models.generate_file_path)),
            ],
            options={
                'ordering': (b'-created',),
                'db_table': b'fileupload_files',
                'verbose_name': 'file',
                'verbose_name_plural': 'files',
                'get_latest_by': b'created',
            },
            bases=(models.Model,),
        ),
    ]
