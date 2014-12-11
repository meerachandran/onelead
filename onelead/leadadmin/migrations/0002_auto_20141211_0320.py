# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leadadmin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='student',
        ),
        migrations.RemoveField(
            model_name='attendance',
            name='time_table_slot',
        ),
        migrations.RemoveField(
            model_name='mentorship',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='mentorship',
            name='student',
        ),
        migrations.DeleteModel(
            name='schedules',
        ),
        migrations.RemoveField(
            model_name='student',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='subjectmap',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='subjectmap',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='batch',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='event',
        ),
        migrations.RemoveField(
            model_name='timetable',
            name='responsible_staff',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='Batch',
        ),
        migrations.DeleteModel(
            name='EventTypes',
        ),
        migrations.DeleteModel(
            name='MentorShip',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='SubjectMap',
        ),
        migrations.DeleteModel(
            name='TimeTable',
        ),
    ]
