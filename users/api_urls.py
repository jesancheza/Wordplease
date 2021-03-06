# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from users.api import UserViewSet

__author__ = 'joseenriquesanchezalfonso'

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
    url(r'api/1.0/', include(router.urls)),  # include de las url's router
]
