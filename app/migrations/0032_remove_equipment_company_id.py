# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 05:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0031_auto_20170213_0519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='company_id',
        ),
    ]
