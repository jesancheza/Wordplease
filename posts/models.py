from django.db import models
from django.utils.datetime_safe import datetime

from blogs.models import Blog

PUBLIC = u'PUB'
PRIVATE = u'PRIV'

POST_TYPE = (
    (PUBLIC, u'Public'),
    (PRIVATE, u'Private')
)


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
    date_published = models.DateTimeField(default=datetime.now)
    category = models.ManyToManyField('Category')
    type = models.CharField(max_length=10, choices=POST_TYPE, default=PUBLIC)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
