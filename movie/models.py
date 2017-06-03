from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
	title = models.CharField(max_length=100)
	score = models.CharField(max_length=50, default='NULL')
	quote = models.CharField(max_length=50)
	image_urls = models.TextField(max_length=500)

	def __unicode__(self):
		return self.title
