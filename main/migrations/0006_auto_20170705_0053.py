# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-05 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170423_2111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('nombre', models.TextField()),
                ('id_empresa', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad_usuarios', models.IntegerField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('username', models.TextField()),
                ('password', models.TextField()),
                ('privilegio', models.IntegerField(default=False)),
                ('id_empresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Xbee',
            fields=[
                ('mac', models.TextField(primary_key=True, serialize=False)),
                ('red', models.TextField()),
                ('tipo', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='information',
            name='id_empresa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Empresa'),
        ),
        migrations.AddField(
            model_name='information',
            name='mac',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Xbee'),
        ),
    ]