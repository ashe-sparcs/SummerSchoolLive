# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 09:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SummerSchoolApp', '0010_auto_20170303_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]