# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-26 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('features', '0017_auto_20190825_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeatureContributors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='contributors',
            name='contributors',
        ),
        migrations.RemoveField(
            model_name='feature',
            name='properties',
        ),
        migrations.AddField(
            model_name='feature',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='feature',
            name='target_value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='feature',
            name='value_collected',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.DeleteModel(
            name='Contributors',
        ),
        migrations.AddField(
            model_name='featurecontributors',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='features.Feature'),
        ),
        migrations.AddField(
            model_name='featurecontributors',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
