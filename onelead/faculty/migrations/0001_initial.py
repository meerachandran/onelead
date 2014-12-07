# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('start_date', models.DateField(verbose_name=b'started_date')),
                ('end_date', models.DateField(verbose_name=b'end_date')),
                ('status', models.CharField(max_length=10)),
                ('currrent_semester', models.CharField(max_length=1)),
            ],
            options=None,
            bases=None,
        ),
    ]
