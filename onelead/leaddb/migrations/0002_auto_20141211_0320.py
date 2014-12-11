# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaddb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='event_date',
        ),
        migrations.AddField(
            model_name='timetable',
            name='subject',
            field=models.ForeignKey(default=None, to='leaddb.Subject'),
            preserve_default=False,
        ),
    ]
