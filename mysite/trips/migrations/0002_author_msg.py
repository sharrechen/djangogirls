# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.contrib.auth.models import User
import trips.models
from datetime import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='post',
            name='traveled_at',
            field=models.DateField(auto_now_add=True, default=datetime.now()),
            preserve_default=True,
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(to='trips.Post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
