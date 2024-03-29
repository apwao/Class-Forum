# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-11 07:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='cover_photos/')),
                ('topic', models.CharField(max_length=200)),
                ('resource_type', models.CharField(choices=[('Book', 'Book'), ('Notes', 'Notes'), ('Slides', 'Slides'), ('Video', 'Video')], default='Book', max_length=200)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('content', models.FileField(upload_to='resources/')),
                ('task', models.CharField(choices=[('Assignment', 'Assignment'), ('Tutorial', 'Tutorial'), ('Cat', 'Cat'), ('Performance_results', 'Performance_results')], default='Notes', max_length=500)),
            ],
        ),
    ]
