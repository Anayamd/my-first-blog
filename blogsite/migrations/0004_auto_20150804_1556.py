# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0003_auto_20150727_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(default='Random', choices=[('Random', 'Random'), ('Intro Programación', 'Intro Programación'), ('Admin', 'Admin'), ('Intro TICs', 'Intro TICs'), ('Matemáticas', 'Matemáticas'), ('Ética', 'Ética')], max_length=12),
        ),
    ]
