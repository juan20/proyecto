# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-04-23 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20170410_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='sensor_sound',
            field=models.IntegerField(default=False),
        ),
    ]
