# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0002_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(default='Random', choices=[('Random', 'Random'), ('Tareas', 'Tareas'), ('Proyectos', 'Proyectos'), ('Juegos', 'Juegos'), ('Hacking', 'Hacking')], max_length=12),
        ),
    ]
