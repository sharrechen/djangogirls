# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20150407_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(default=datetime.datetime(2015, 4, 7, 15, 12, 5, 761223), auto_now_add=True),
            preserve_default=True,
        ),
    ]
