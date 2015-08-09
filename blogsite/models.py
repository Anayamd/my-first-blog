from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	#tag options
	_random = 'Random'
	_IPS = 'IPS'
	_Admin = 'Admin'
	_TICs = 'Intro_TICs'
	_Mate = 'Matemáticas'
	_Etica = 'Ética'
	tag_choices = (
		(_random, 'Random'),
		(_IPS, 'IPS'),
		(_Admin, 'Admin'),
		(_TICs, 'Intro_TICs'),
		(_Mate, 'Matemáticas'),
		(_Etica, 'Ética'),
		)

	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	tags = models.CharField(choices=tag_choices, default=_random, max_length=140)
	docfile = models.FileField(null=True, blank=True, upload_to='documents')

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey('blogsite.Post', related_name='comments')	
	author = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.text