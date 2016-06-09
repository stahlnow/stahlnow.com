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
                'db_table': 'blog_categories',
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('slug', models.SlugField(verbose_name='slug', unique_for_date=b'publish')),
                ('body', ckeditor.fields.RichTextField(verbose_name='body')),
                ('tease', ckeditor.fields.RichTextField(help_text='Concise text suggested. Does not appear in RSS feed.', verbose_name='tease', blank=True)),
                ('status', models.IntegerField(default=2, verbose_name='status', choices=[(1, 'Draft'), (2, 'Public')])),
                ('allow_comments', models.BooleanField(default=True, verbose_name='allow comments')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='publish')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('categories', models.ManyToManyField(to='blog.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
                'db_table': 'blog_posts',
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
                'get_latest_by': 'publish',
            },
            bases=(models.Model,),
        ),
    ]
