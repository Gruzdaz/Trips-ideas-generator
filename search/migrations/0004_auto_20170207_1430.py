# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-02-07 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_trip_youtube_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='trip',
            name='youtube_url',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
