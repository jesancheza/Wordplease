#-*- coding: utf-8 -*-
from blogs.models import Blog
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    blogs = Blog.objects.all()

    html = "<ul>"
    for blog in blogs:
        html += "<li> Blog de " + +"</li>"

    html += "</ul>"
    return HttpResponse(html)