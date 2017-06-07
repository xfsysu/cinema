from django.db import models
from django.contrib.auth import get_user_model

class Movie(models.Model):
	mName = models.CharField(max_length=100)
	director = models.CharField(max_length=100)
	performer = models.CharField(max_length=100)
	duration = models.CharField(max_length=10)
	score = models.CharField(max_length=50, default='NULL')
	brief = models.TextField(max_length=500)
	price = models.CharField(max_length=10)
	image_urls = models.TextField(max_length=500)

	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movies'

	def __unicode__(self):
		return self.mName


class Comment(models.Model):
	movie = models.ForeignKey(Movie, related_name='comment')
	user = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
	content = models.TextField(max_length=500)
	created_time = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comments'
		ordering = ('created_time',)

	def __unicode__(self):
		return self.content


class Order(models.Model):
	movie = models.ForeignKey(Movie)
	user = models.ForeignKey('auth.User', related_name='orders', on_delete=models.CASCADE)
	created_time = models.DateTimeField(auto_now_add=True)
	price = models.CharField(max_length=10)
	isPay = models.BooleanField(default=False)

	class Meta:
		ordering = ('created_time',)

