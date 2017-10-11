# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_auto_20170731_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectcohort',
            name='cohort',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_project', to='patients.Cohort'),
        ),
        migrations.AlterField(
            model_name='projectcohort',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_cohorts', to='patients.Project'),
        ),
    ]