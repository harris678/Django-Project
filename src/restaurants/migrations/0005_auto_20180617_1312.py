# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-17 07:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_restaurantlocation_owners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocation',
            name='owners',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
