# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import fileupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0004_file_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/files/', location=b'/home/stahl/web/stahlnow/website/media/files'), upload_to=fileupload.models.generate_file_path),
            preserve_default=True,
        ),
    ]
