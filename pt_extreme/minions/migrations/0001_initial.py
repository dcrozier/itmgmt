# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-17 00:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Minion',
            fields=[
                ('mac_address', models.CharField(max_length=17, primary_key=True, serialize=False)),
                ('public_ip', models.GenericIPAddressField()),
                ('private_ip', models.GenericIPAddressField()),
                ('host_name', models.CharField(max_length=50)),
            ],
        ),
    ]
