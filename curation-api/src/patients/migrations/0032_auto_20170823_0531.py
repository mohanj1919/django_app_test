# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-23 05:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0031_appointment_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='start',
            field=models.CharField(max_length=100),
        ),
    ]
