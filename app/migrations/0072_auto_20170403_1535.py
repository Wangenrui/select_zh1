# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-03 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0071_auto_20170403_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finger',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
