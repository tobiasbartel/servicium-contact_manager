# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0002_auto_20161019_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactoptions',
            name='value',
            field=models.CharField(max_length=100),
        ),
    ]
