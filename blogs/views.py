#-*- coding: utf-8 -*-
from django.db.models import Prefetch
from django.views.generic import View

from blogs.models import Blog
from django.http import HttpResponseNotFound
from django.shortcuts import render

from posts.models import Post


class BlogUserView(View):

    def get(self, request):
        blogs = Blog.objects.all()
        context = {
            'blogs': blogs
        }

        return render(request, 'blogs/blogs.html', context)


class BlogDetailView(View):

    def get(self, request, username):
        posible_blog = Blog.objects.filter(owner__username=username).prefetch_related(
            Prefetch('posts', queryset=Post.objects.order_by('-created_at')))
        blog = posible_blog[0] if len(posible_blog) >= 1 else None
        if blog is not None:
            context = {
                'blog': blog
            }
            return render(request, 'blogs/detail.html', context)
        else:
            return HttpResponseNotFound('Este blog no tiene posts.')
