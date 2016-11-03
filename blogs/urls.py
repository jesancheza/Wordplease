# -*- coding: utf-8 -*-
from django.conf.urls import url

from blogs.views import BlogUserView, BlogDetailView

urlpatterns = [
    # Blog URLs
    url(r'^blogs$', BlogUserView.as_view(), name='blogs_home'),
    url(r'^blogs/(?P<username>[-\w]+)/$', BlogDetailView.as_view(), name='detail_blog')
]