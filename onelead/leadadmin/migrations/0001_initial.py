# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('added_date', models.DateTimeField()),
                ('event_date', models.DateField()),
                ('source_device', models.CharField(max_length=200)),
                ('status_of_student', models.CharField(max_length=10)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name=b'started_date')),
                ('end_date', models.DateField(verbose_name=b'end_date')),
                ('status', models.CharField(max_length=10)),
                ('currrent_semester', models.CharField(max_length=10)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='EventTypes',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='MentorShip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='schedules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date_time', models.DateTimeField(verbose_name=b'start_date')),
                ('end_date_time', models.DateTimeField(verbose_name=b'end_date')),
                ('geo_location', models.CharField(max_length=50)),
                ('notify', models.CharField(max_length=5)),
                ('summary', models.CharField(max_length=200)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('emp_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=200)),
                ('emergency_phone_no', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('education_history', models.CharField(max_length=200)),
                ('joined_date', models.DateField(verbose_name=b'joined_date')),
                ('emp_type', models.CharField(max_length=20)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('admission_no', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=1)),
                ('address', models.CharField(max_length=200)),
                ('emergency_phone_no', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('parents', models.CharField(max_length=200)),
                ('education_history', models.CharField(max_length=200)),
                ('admitted_date', models.DateField(verbose_name=b'admitted_date')),
                ('batch', models.ForeignKey(to='leadadmin.Batch')),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='SubjectMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('batch', models.ForeignKey(to='leadadmin.Batch')),
                ('subject', models.ForeignKey(to='leadadmin.Subject')),
            ],
            options=None,
            bases=None,
        ),
        migrations.CreateModel(
            name='TimeTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date_time', models.DateTimeField()),
                ('end_date_time', models.DateTimeField()),
                ('geo_location', models.CharField(max_length=50)),
                ('notify', models.CharField(max_length=5)),
                ('summary', models.CharField(max_length=200)),
                ('batch', models.ForeignKey(to='leadadmin.Batch')),
                ('event', models.ForeignKey(to='leadadmin.EventTypes')),
                ('responsible_staff', models.ForeignKey(to='leadadmin.Staff')),
            ],
            options=None,
            bases=None,
        ),
        migrations.AddField(
            model_name='mentorship',
            name='staff',
            field=models.ForeignKey(to='leadadmin.Staff'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='mentorship',
            name='student',
            field=models.ForeignKey(to='leadadmin.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(to='leadadmin.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='attendance',
            name='time_table_slot',
            field=models.ForeignKey(to='leadadmin.TimeTable'),
            preserve_default=True,
        ),
    ]
