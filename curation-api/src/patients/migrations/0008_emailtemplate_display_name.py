# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-09 13:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20170809_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailtemplate',
            name='display_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
