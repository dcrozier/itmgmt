# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-14 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='docfile',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
