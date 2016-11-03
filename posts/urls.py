# -*- coding: utf-8 -*-
from django.conf.urls import url

from posts.views import HomeView, PostCreateView, PostDetailView

__author__ = 'joseenriquesanchezalfonso'

urlpatterns = [
    # Post URLs
    url(r'^$', HomeView.as_view(), name='wordplease_home'),
    url(r'^blogs/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', PostDetailView.as_view(), name='post_detail'),
    url(r'^new-post$', PostCreateView.as_view(), name='create_post')
]