# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='body',
            field=models.TextField(verbose_name='body'),
        ),
    ]
