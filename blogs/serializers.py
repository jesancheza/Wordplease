# -*- coding: utf-8 -*-
from rest_framework import serializers
from rest_framework.reverse import reverse

from blogs.models import Blog

__author__ = 'joseenriquesanchezalfonso'


class BlogSerializer(serializers.ModelSerializer):

    title = serializers.CharField()
    description = serializers.CharField()
    blog_url = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = ('title', 'description', 'blog_url')

    def get_blog_url(self, obj):
        return self.context['request'].build_absolute_uri(reverse('detail_blog', kwargs={'username': obj.owner}))
