# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from blogs.models import Blog
from blogs.serializers import BlogSerializer

__author__ = 'joseenriquesanchezalfonso'


class BlogsViewSet(GenericViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('owner__first_name', )
    ordering_fields = ('title', 'owner__first_name')

    def list(self, request):

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
