# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-11 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resources',
            name='task',
            field=models.CharField(choices=[('Assignment', 'Assignment'), ('Tutorial', 'Tutorial'), ('Cat', 'Cat'), ('Performance_results', 'Performance_results'), ('Reading_Assignment', 'Reading_Assignment')], default='Notes', max_length=500),
        ),
    ]
