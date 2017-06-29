# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 15:57
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='updated',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True),
        ),
    ]
