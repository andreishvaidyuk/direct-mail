# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-27 04:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery_letter', '0004_auto_20180127_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='letter',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]