
# blog/models.py
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField('Tag')
    category = models.ForeignKey('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_model_field = False

    def __str__(self):
   		return '{} - {} - {}'.format(self.pk, self.title, self.category.pk)

class Comment(models.Model):
	post = models.ForeignKey(Post)
	content = models.TextField(max_length=500)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('pk', '-updated_at')

	def __str__(self):
   		return '{} - {} - {}'.format(self.pk, self.post.pk, self.content)

class Tag(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
   		return '{} - {}'.format(self.pk, self.name)

class Category(models.Model):
	name = models.CharField(max_length=40)

	def __str__(self):
		return '{} - {}'.format(self.pk, self.name)



		
		


