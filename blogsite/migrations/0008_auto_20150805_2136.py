# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0007_auto_20150804_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='docfile',
            field=models.FileField(upload_to='documents', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(choices=[('Random', 'Random'), ('Intro Programación', 'Intro Programación'), ('Admin', 'Admin'), ('Intro TICs', 'Intro TICs'), ('Matemáticas', 'Matemáticas'), ('Ética', 'Ética')], max_length=25, default='Random'),
        ),
    ]
