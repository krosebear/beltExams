# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 22:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20170928_0138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='likes',
        ),
    ]