# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-10 17:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20161206_1524'),
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorderline',
            name='discount',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='salesorderline',
            name='unit_of_measurement',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='product.UnitOfMeasurement'),
            preserve_default=False,
        ),
    ]
