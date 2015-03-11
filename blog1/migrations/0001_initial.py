# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, blank=True)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['modified_time'],
                'db_table': 'blog',
                'verbose_name': '\u535a\u5ba2',
                'verbose_name_plural': '\u535a\u5ba2',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('category_name', models.CharField(max_length=200)),
                ('category_description', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['modified_time'],
                'db_table': 'category',
                'verbose_name': '\u5206\u7c7b',
                'verbose_name_plural': '\u5206\u7c7b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('content', models.CharField(max_length=250)),
                ('blog_id', models.ForeignKey(to='blog1.Blog')),
            ],
            options={
                'ordering': ['modified_time'],
                'db_table': 'comment',
                'verbose_name': '\u8bc4\u8bba',
                'verbose_name_plural': '\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=75)),
                ('content', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ['modified_time'],
                'db_table': 'message',
                'verbose_name': '\u7559\u8a00',
                'verbose_name_plural': '\u7559\u8a00',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now=True)),
                ('nick_name', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200, blank=True)),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('location', models.CharField(max_length=200, blank=True)),
                ('qq', models.IntegerField(null=True)),
                ('weibo', models.CharField(max_length=200, blank=True)),
                ('job', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'ordering': ['modified_time'],
                'db_table': 'profile',
                'verbose_name': '\u4e2a\u4eba\u8d44\u6599',
                'verbose_name_plural': '\u4e2a\u4eba\u8d44\u6599',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(to='blog1.Category'),
            preserve_default=True,
        ),
    ]
