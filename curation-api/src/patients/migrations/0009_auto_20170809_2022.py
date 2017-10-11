# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-09 14:52
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings

def load_stores_from_sql():
    import os
    sql_statements = open(os.path.join(str(settings.APPS_DIR), 'patients/sql/email_templates.sql'), 'r').read()
    return sql_statements

class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0008_emailtemplate_display_name'),
    ]

    operations = [
        migrations.RunSQL(load_stores_from_sql()),
    ]