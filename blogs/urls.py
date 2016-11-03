# -*- coding: utf-8 -*-
from django.conf.urls import url

urlpatterns = [
    # Blog URLs
    url(r'^blogs$', 'blogs.views.home', name='blogs_home'),
    url(r'^blogs/(?P<username>[-\w]+)/$', 'blogs.views.detail', name='detail_blog')
]