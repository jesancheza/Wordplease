# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from blogs.api import BlogsViewSet

__author__ = 'joseenriquesanchezalfonso'

router = DefaultRouter()
router.register('blog', BlogsViewSet)

urlpatterns = [
    url(r'1.0/', include(router.urls)),  # include de las url's router
]