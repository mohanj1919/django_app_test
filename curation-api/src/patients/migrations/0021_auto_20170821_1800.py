# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 12:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0020_auto_20170821_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encounter',
            old_name='cohort_id',
            new_name='cohort',
        ),
        migrations.RenameField(
            model_name='encounter',
            old_name='patient_id',
            new_name='patient',
        ),
    ]