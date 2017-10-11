# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-30 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0037_auto_20170829_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='status',
            field=models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive'), ('Resolved', 'Resolved'), ('Active diagnosis', 'Active diagnosis'), ('Resolved diagnosis', 'Resolved diagnosis')], default=None, max_length=100, null=True),
        ),
    ]
