# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-16 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20170715_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='negocio',
            name='longitud',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='negocio',
            name='nombre',
            field=models.TextField(default=''),
        ),
    ]
