# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favor',
            name='ctime',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]