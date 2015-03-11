# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='blog_id',
            new_name='blog',
        ),
        migrations.AlterField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x9c\xe8\x80\x85'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blog',
            name='views',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe6\x8f\x8f\xe8\xbf\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\x88\x86\xe7\xb1\xbb\xe5\x90\x8d\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='content',
            field=models.CharField(max_length=250, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=20, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=75, verbose_name=b'\xe9\x82\xae\xe7\xae\xb1', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='job',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\xb7\xa5\xe4\xbd\x9c', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(max_length=200, verbose_name=b'\xe4\xbd\x8d\xe7\xbd\xae', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='nick_name',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\xa4\xb4\xe5\x83\x8f', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='qq',
            field=models.IntegerField(null=True, verbose_name=b'QQ'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='profile',
            name='weibo',
            field=models.CharField(max_length=200, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a', blank=True),
            preserve_default=True,
        ),
    ]
