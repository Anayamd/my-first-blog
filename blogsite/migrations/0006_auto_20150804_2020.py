# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0005_post_docfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(upload_to='documents/%Y/%m/%d', null=True),
        ),
    ]
