# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-24 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0006_contributors'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='contributors',
            field=models.CharField(default='0', max_length=254),
        ),
    ]
