# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-10 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0002_auto_20190902_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit_card_number', models.CharField(max_length=17)),
                ('cvv', models.CharField(max_length=4)),
                ('expiry_month', models.DateField()),
                ('expiry_year', models.DateField()),
                ('stripe_id', models.CharField(max_length=250)),
            ],
        ),
    ]
