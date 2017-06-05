from __future__ import unicode_literals

from django.db import models

class Movie(models.Model):
	mName = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	performer = models.CharField(max_length=100)
	duration = models.CharField(max_length=10)
	score = models.CharField(max_length=50, default='NULL')
	brief = models.TextField(max_length=500)
	image_urls = models.TextField(max_length=500)

	def __unicode__(self):
		return self.mName


class Comment(models.Model):
	movie = models.ForeignKey(Movie, related_name='comments', on_delete=models.CASCADE)
	content = models.TextField(max_length=500)

	def __unicode__(self):
		return self.content


