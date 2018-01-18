# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 03:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0065_auto_20170305_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoAccessType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='videocamera',
            name='access_type',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.VideoAccessType'),
            preserve_default=False,
        ),
    ]
