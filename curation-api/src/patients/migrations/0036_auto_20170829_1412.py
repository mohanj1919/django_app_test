# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-29 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0035_auto_20170824_0750'),
    ]

    operations = [
        migrations.AddField(
            model_name='encounter',
            name='provider_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='provider',
            name='provider_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='data_source_id',
            field=models.IntegerField(),
        ),
    ]
