# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields
import django.utils.timezone
from django.conf import settings
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('fileupload', '0005_auto_20150330_1902'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('slug', models.SlugField(unique=True, verbose_name='slug')),
            ],
            options={
                'ordering': ('title',),
                'db_table': 'project_categories',
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug', unique_for_date=b'publish')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Draft'), (2, 'Public')])),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('my_order', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(to='projects.Category', null=True)),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
                ('teaser', models.ForeignKey(to='fileupload.File')),
            ],
            options={
                'ordering': ('my_order',),
                'db_table': 'project_projects',
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'get_latest_by': 'publish',
            },
            bases=(models.Model,),
        ),
    ]
