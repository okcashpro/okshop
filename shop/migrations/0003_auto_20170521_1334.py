# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-21 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20170520_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delete_on_over',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='removed',
            field=models.BooleanField(default=False),
        ),
    ]
