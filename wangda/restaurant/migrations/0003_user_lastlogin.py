# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lastLogin',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
