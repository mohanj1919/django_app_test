# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-28 10:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170824_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='curationuser',
            name='created_by',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='curationuser',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AddField(
            model_name='curationuser',
            name='updated_by',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='curationuser',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, db_index=True, null=True),
        ),
    ]
