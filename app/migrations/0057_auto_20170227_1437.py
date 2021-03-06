# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-27 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0056_meterialrecord_resource_sub_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='materialsubtype',
            name='code',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='materialsubtype',
            name='prompt',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='materialsubtype',
            name='type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.MaterialType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='materialsubtype',
            name='unit_type',
            field=models.SmallIntegerField(default=0),
        ),
    ]
