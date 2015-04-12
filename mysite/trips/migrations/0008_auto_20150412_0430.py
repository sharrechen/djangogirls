# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_auto_20150412_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='email',
        ),
        migrations.RemoveField(
            model_name='author',
            name='facebook',
        ),
        migrations.RemoveField(
            model_name='author',
            name='github',
        ),
        migrations.RemoveField(
            model_name='author',
            name='name',
        ),
        migrations.RemoveField(
            model_name='author',
            name='twitter',
        ),
        migrations.AddField(
            model_name='author',
            name='facebook_link',
            field=models.URLField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='github_link',
            field=models.URLField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='twitter_link',
            field=models.URLField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 4, 12, 4, 30, 55, 12043)),
            preserve_default=True,
        ),
    ]
