# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 17:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20170115_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='redeeming_instructions',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]