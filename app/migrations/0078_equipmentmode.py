# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-23 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0077_seismometer'),
    ]

    operations = [
        migrations.CreateModel(
            name='EquipmentMode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Equipment Mode')),
            ],
        ),
    ]
