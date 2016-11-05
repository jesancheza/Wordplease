# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet

from blogs.models import Blog
from posts.models import Post
from posts.permissions import PostPermissions
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostQueryset

__author__ = 'joseenriquesanchezalfonso'


class PostViewSet(PostQueryset, ModelViewSet):

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = (PostPermissions, )

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('title', 'body')
    ordering_fields = ('title', 'date_published')

    def get_queryset(self):
        return self.get_post_queryset(self.request)

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        else:
            return PostSerializer

    def perform_create(self, serializer):
        blog = Blog.objects.filter(owner=self.request.user).first()
        serializer.save(blog=blog)
