# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0006_auto_20150804_2020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
    ]
