# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 16:30
from __future__ import unicode_literals

from django.db import migrations, models

from .. import app_settings


OPERATIONS = []

if app_settings.ENABLE_CODECOV:
    OPERATIONS.append(migrations.CreateModel(
        name='Codecov',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('coverage', models.PositiveIntegerField()),
            ('hit', models.PositiveIntegerField()),
            ('partial', models.PositiveIntegerField()),
            ('branches', models.PositiveIntegerField()),
            ('lines', models.PositiveIntegerField()),
            ('missed', models.PositiveIntegerField()),
            ('files', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))

if app_settings.ENABLE_GIT:
    OPERATIONS.append(migrations.CreateModel(
        name='Git',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('nb_commits', models.PositiveIntegerField()),
            ('nb_files', models.PositiveIntegerField()),
            ('nb_lines', models.PositiveIntegerField()),
            ('nb_dirs', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))

if app_settings.ENABLE_PIVOTAL:
    OPERATIONS.append(migrations.CreateModel(
        name='Pivotal',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('nb_stories', models.PositiveIntegerField()),
            ('total_points', models.PositiveIntegerField()),
            ('nb_features', models.PositiveIntegerField()),
            ('nb_bugs', models.PositiveIntegerField()),
            ('nb_chores', models.PositiveIntegerField()),
            ('nb_releases', models.PositiveIntegerField()),
            ('nb_delivered_stories', models.PositiveIntegerField()),
            ('nb_finished_stories', models.PositiveIntegerField()),
            ('nb_rejected_stories', models.PositiveIntegerField()),
            ('nb_started_stories', models.PositiveIntegerField()),
            ('nb_unstarted_stories', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))

if app_settings.ENABLE_PROSPECTOR:
    OPERATIONS.append(migrations.CreateModel(
        name='Prospector',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('nb_messages', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))

if app_settings.ENABLE_SENTRY:
    OPERATIONS.append(migrations.CreateModel(
        name='Sentry',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('nb_unresolved_issues', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))

if app_settings.ENABLE_ZENDESK:
    OPERATIONS.append(migrations.CreateModel(
        name='Zendesk',
        fields=[
            ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ('app_name', models.TextField()),
            ('datetime', models.DateTimeField()),
            ('nb_tickets', models.PositiveIntegerField()),
            ('nb_urgent_tickets', models.PositiveIntegerField()),
            ('nb_high_tickets', models.PositiveIntegerField()),
            ('nb_normal_tickets', models.PositiveIntegerField()),
            ('nb_low_tickets', models.PositiveIntegerField()),
            ('nb_new_tickets', models.PositiveIntegerField()),
            ('nb_open_tickets', models.PositiveIntegerField()),
            ('nb_pending_tickets', models.PositiveIntegerField()),
            ('nb_hold_tickets', models.PositiveIntegerField()),
        ],
        options={
            'ordering': ('-datetime',),
            'abstract': False,
            'get_latest_by': 'datetime',
        },
    ))


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = OPERATIONS
