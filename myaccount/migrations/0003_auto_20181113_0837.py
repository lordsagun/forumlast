# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-11-13 02:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_auto_20180924_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
    ]
