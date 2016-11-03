# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):

    owner = models.OneToOneField(User)
    title = models.TextField(max_length=150)
    description = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title
