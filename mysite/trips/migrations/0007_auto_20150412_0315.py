# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0006_auto_20150409_1431'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='id',
        ),
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 4, 12, 3, 15, 12, 911812)),
            preserve_default=True,
        ),
    ]
