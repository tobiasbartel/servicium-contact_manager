# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 18:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0004_auto_20161019_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='is_memeber_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_of_team', to='contact_manager.Contact'),
        ),
    ]
