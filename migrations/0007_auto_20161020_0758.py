# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-20 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_manager', '0006_auto_20161019_2000'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=15)),
                ('image', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='is_memeber_of',
            new_name='is_member_of',
        ),
    ]
