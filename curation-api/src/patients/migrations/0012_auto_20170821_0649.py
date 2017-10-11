# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0011_auto_20170809_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='address_state',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='deceased_indicator',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='employment_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='ethnicity',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='language',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='living_situation_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='marital_status',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='pcp_id',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='sex',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='year_of_birth',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='year_of_death',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='zip_3',
        ),
        migrations.AddField(
            model_name='patient',
            name='date_of_birth',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='deceased',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='dob_is_year',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='patient',
            name='sex_at_birth',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Unknown', 'Unknown'), ('Other ', 'Other')], max_length=10, null=True),
        ),
    ]