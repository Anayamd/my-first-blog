# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogsite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.CharField(default='rand', max_length=4, choices=[('rand', 'Random'), ('h.w.', 'Tareas'), ('proj', 'Proyectos'), ('game', 'Juegos'), ('hack', 'Hacking')]),
        ),
    ]
