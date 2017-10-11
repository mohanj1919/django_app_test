# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 10:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0027_auto_20170822_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Resolved', 'Resolved')], default=None, max_length=100, null=True),
        ),
    ]
