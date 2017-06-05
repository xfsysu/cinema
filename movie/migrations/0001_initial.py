# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-05 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mName', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('performer', models.CharField(max_length=100)),
                ('duration', models.IntegerField(default=0)),
                ('score', models.CharField(default='NULL', max_length=50)),
                ('brief', models.TextField(max_length=500)),
                ('image_urls', models.TextField(max_length=500)),
            ],
        ),
    ]
