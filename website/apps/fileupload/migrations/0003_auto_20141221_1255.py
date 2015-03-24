# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import fileupload.models


class Migration(migrations.Migration):

    dependencies = [
        ('fileupload', '0002_auto_20141104_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(storage=django.core.files.storage.FileSystemStorage(base_url=b'/media/', location=b'/home/stahl/web/stahlnow/website/media'), upload_to=fileupload.models.generate_file_path),
            preserve_default=True,
        ),
    ]
