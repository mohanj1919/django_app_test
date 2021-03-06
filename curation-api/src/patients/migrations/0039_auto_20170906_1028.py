# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-09-06 10:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0038_auto_20170830_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='patient_events', to='patients.Patient'),
        ),
        migrations.AlterField(
            model_name='event',
            name='appointments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointment_events', to='patients.Appointment'),
        ),
        migrations.AlterField(
            model_name='event',
            name='encounters',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='encounter_events', to='patients.Encounter'),
        ),
        migrations.AlterField(
            model_name='event',
            name='module_instances',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='module_events', to='patients.ModuleInstance'),
        ),
        migrations.AlterField(
            model_name='projectcohortpatient',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_project_cohort', to='patients.Patient'),
        ),
    ]
