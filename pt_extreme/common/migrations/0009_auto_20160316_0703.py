# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 07:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_auto_20160316_0511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recentactions',
            name='input_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 7, 3, 23, 763144, tzinfo=utc)),
        ),
    ]
