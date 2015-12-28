# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-24 18:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marcador', '0003_auto_20151224_2358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='Longitude',
        ),
        migrations.AddField(
            model_name='route',
            name='latitude',
            field=models.CharField(default=1, max_length=512, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='route',
            name='longitude',
            field=models.CharField(default=1, max_length=512, verbose_name='Longitude'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='route',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Bus Route'),
        ),
        migrations.AlterField(
            model_name='route',
            name='url',
            field=models.URLField(max_length=255, verbose_name='Click me to connect with google maps?'),
        ),
    ]