from django.db import models
from blogs.models import Blog


class Category(models.Model):

    title = models.CharField(max_length=150)
    short_description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class Post(models.Model):

    blog = models.ForeignKey(Blog, related_name="posts")
    title = models.CharField(max_length=150)
    summary = models.TextField(max_length=400)
    body = models.TextField(default='')
    image_url = models.URLField(blank=True, null=True, default="")
    date_published = models.DateTimeField(default='')
    category = models.ManyToManyField('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
