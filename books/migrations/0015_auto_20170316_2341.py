# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 06:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_auto_20170316_2327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll_no',
            field=models.CharField(max_length=10),
        ),
    ]
