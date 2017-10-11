# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-22 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0024_auto_20170822_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnosis',
            name='code_type',
            field=models.CharField(choices=[('ICD9_Diagnosis', 'ICD9 Diagnosis'), ('ICD10_Diagnosis', 'ICD10 Diagnosis'), ('MEDCIN', 'MEDCIN'), ('SNOMED', 'SNOMED')], max_length=100),
        ),
        migrations.AlterField(
            model_name='patient',
            name='deceased',
            field=models.NullBooleanField(default=False),
        ),
    ]