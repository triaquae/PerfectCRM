# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-30 05:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beeflow', '0008_auto_20170430_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='role',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beeflow.FlowRole', verbose_name='审批角色'),
            preserve_default=False,
        ),
    ]
