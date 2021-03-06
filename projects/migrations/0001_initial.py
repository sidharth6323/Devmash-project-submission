# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_name', models.CharField(max_length=500)),
                ('p_description', models.TextField()),
                ('deadline', models.DateTimeField()),
                ('track', models.CharField(choices=[('python', 'python'), ('android', 'android'), ('web', 'web')], max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_uname', models.CharField(max_length=100)),
                ('s_uname', models.CharField(max_length=100)),
                ('f_name', models.CharField(max_length=100)),
                ('track', models.CharField(choices=[('python', 'python'), ('android', 'android'), ('web', 'web')], max_length=500)),
                ('p_submitted', models.ManyToManyField(to='projects.project')),
            ],
        ),
    ]
