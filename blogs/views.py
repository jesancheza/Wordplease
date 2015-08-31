#-*- coding: utf-8 -*-
from blogs.models import Blog
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }

    return render(request, 'blogs/blogs.html', context)

def detail(request, pk):
    posible_blog = Blog.objects.filter(owner=pk)
    blog = posible_blog[0] if len(posible_blog) >= 1 else None
    if blog is not None:
        context = {
            'blog': blog
        }
        return render(request, 'detail_blog', context)
    else:
        return HttpResponseNotFound('No existe el blog.')