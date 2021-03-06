# -*- coding: utf-8 -*-
# Generated by Django 1.10rc1 on 2017-01-22 20:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('continent', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TripImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='search.Trip')),
            ],
        ),
    ]
