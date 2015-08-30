from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):

    owner = models.OneToOneField(User)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
