# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-06 15:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_auto_20161005_1348'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
