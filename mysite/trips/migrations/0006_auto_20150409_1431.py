# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0005_auto_20150407_1512'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='facebook',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='github',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='twitter',
            field=models.CharField(max_length=100, default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(default=datetime.datetime(2015, 4, 9, 14, 31, 45, 491194), auto_now_add=True),
            preserve_default=True,
        ),
    ]
