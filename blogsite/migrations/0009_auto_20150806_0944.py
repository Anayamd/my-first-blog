# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0008_auto_20150805_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(default='Random', choices=[('Random', 'Random'), ('IPS', 'IPS'), ('Admin', 'Admin'), ('Intro_TICs', 'Intro_TICs'), ('Matemáticas', 'Matemáticas'), ('Ética', 'Ética')], max_length=30),
        ),
    ]
