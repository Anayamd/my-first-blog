# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0004_auto_20150804_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, blank=True, upload_to='documents/%Y/%m/%d'),
        ),
    ]
