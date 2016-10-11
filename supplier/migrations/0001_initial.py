# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-11 22:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('organization_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='contact.Organization')),
                ('products', models.ManyToManyField(to='product.Product')),
            ],
            options={
                'abstract': False,
            },
            bases=('contact.organization',),
        ),
    ]
