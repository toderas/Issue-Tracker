# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-25 12:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0011_auto_20190825_1214'),
    ]

    operations = [
        migrations.AddField(
            model_name='contributors',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
