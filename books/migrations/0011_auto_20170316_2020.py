# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-17 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='std',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='branch',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='year',
            field=models.CharField(blank=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roll_no',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
