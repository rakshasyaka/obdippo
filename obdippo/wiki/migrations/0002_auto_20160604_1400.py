# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
