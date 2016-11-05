# -*- coding: utf-8 -*-
from rest_framework import serializers

from posts.models import Post

__author__ = 'joseenriquesanchezalfonso'


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('title', 'image_url', 'summary', 'date_published')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = ('blog', )
