# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-21 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0021_auto_20170821_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='documenting_provider_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='microbio_antibiotic',
        ),
        migrations.RemoveField(
            model_name='result',
            name='microbio_mic',
        ),
        migrations.RemoveField(
            model_name='result',
            name='microbio_organism',
        ),
        migrations.RemoveField(
            model_name='result',
            name='microbio_sensitivity',
        ),
        migrations.RemoveField(
            model_name='result',
            name='order_code',
        ),
        migrations.RemoveField(
            model_name='result',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='performing_provider_id',
        ),
        migrations.RemoveField(
            model_name='result',
            name='reference_range_lower',
        ),
        migrations.RemoveField(
            model_name='result',
            name='reference_range_upper',
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='diagnoses', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='jointexam',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='joint_exams', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='medication',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='note',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='observation',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='observations', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='procedures', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questionnaires', to='patients.Encounter'),
        ),
        migrations.AddField(
            model_name='result',
            name='patient_encounter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='results', to='patients.Encounter'),
        ),
    ]
