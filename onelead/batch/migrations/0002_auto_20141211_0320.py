# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='currrent_semester',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
