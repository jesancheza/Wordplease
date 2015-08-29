#-*- coding: utf-8 -*-
from blogs.models import Blog
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    blogs = Blog.objects.all()
    context = {
        'blogs': blogs
    }

    return render(request, 'blogs/blogs.html', context)