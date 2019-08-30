# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-25 13:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0016_auto_20190825_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='properties',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contributor', to='features.Contributors'),
        ),
    ]