# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-10-04 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20161005_0231'),
    ]

    operations = [
        migrations.CreateModel(
            name='s_project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repo_link', models.CharField(max_length=500)),
                ('hosted_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='hosted_url',
        ),
        migrations.RemoveField(
            model_name='project',
            name='repo_link',
        ),
        migrations.AddField(
            model_name='s_project',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project'),
        ),
        migrations.AddField(
            model_name='s_project',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.users'),
        ),
    ]