# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-09 03:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0004_auto_20181123_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='re_password',
            field=models.CharField(max_length=30),
        ),
    ]
