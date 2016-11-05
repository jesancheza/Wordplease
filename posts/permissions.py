# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

__author__ = 'joseenriquesanchezalfonso'


class PostPermissions(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        elif view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['create', 'update', 'destroy'] and request.user.is_authenticated():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if request.user.is_superuser:
            return True
        elif view.action in ['list', 'retrieve']:
            return True
        elif view.action in ['destroy', 'update'] and (request.user == obj.blog.owner or request.user.is_superuser):
            return True
        else:
            return False
