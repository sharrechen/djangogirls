# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20150407_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='author',
            name='nation',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(default=datetime.datetime(2015, 4, 7, 15, 4, 35, 74909), auto_now_add=True),
            preserve_default=True,
        ),
    ]
