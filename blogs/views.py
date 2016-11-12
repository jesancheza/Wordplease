#-*- coding: utf-8 -*-
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
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
        # posible_blog = Blog.objects.filter(owner__username=username).prefetch_related(
        #    Prefetch('posts', queryset=Post.objects.order_by('-created_at')))
        posible_blog = Blog.objects.filter(owner__username=username)
        blog = posible_blog[0] if len(posible_blog) >= 1 else None
        if blog is not None:
            posts = Post.objects.filter(blog__owner__username=username).order_by('-date_published')
            paginator = Paginator(posts, 3)  # Show 3 posts per page

            page = request.GET.get('page')
            try:
                posts = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                posts = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                posts = paginator.page(paginator.num_pages)
            context = {
                'blog': blog,
                'posts': posts
            }
            return render(request, 'blogs/detail.html', context)
        else:
            return HttpResponseNotFound('Este blog no tiene posts.')
