from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	#tag options
	_random = 'Random'
	_tareas = 'Tareas'
	_proyectos = 'Proyectos'
	_juegos = 'Juegos'
	_hacking = 'Hacking'
	tag_choices = (
		(_random, 'Random'),
		(_tareas, 'Tareas'),
		(_proyectos, 'Proyectos'),
		(_juegos, 'Juegos'),
		(_hacking, 'Hacking'),
		)

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(choices=tag_choices, default=_random, max_length=12)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title