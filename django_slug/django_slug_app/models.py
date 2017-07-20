from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify

class Post(models.Model):
	name = models.CharField(max_length = 20)
	title = models.CharField(max_length = 20)
	sub_title = models.CharField(max_length = 20)
	slug = models.SlugField(unique = True, null = True)
	
	def __str__(self):
		return self.name

# create a automatic slug field
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Post, self).save(*args, **kwargs)

# return slug on url
	def get_absolute_url(self):
		return reverse('detail', kwargs={'slug':self.slug})