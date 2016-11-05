# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from posts.api import PostViewSet

__author__ = 'joseenriquesanchezalfonso'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    url(r'api/1.0/', include(router.urls)),  # include de las url's router
]
