# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 04:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_auto_20170223_2027'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
