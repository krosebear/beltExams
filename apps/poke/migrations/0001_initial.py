# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 22:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0006_remove_user_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('give', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gavePoke', to='main.User')),
                ('recieve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gotPoke', to='main.User')),
            ],
        ),
    ]
