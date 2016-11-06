# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission

__author__ = 'joseenriquesanchezalfonso'


class UserPermissions(BasePermission):

    def has_permission(self, request, view):

        if request.user.is_superuser:
            return True
        elif view.action in ['create']:
            return True
        elif view.action in ['retrieve', 'destroy', 'update'] and request.user.is_authenticated():
            return True
        else:
            return False

    def has_object_permission(self, request, view, obj):

        if view.action in ['create']:
            return True
        elif view.action in ['retrieve', 'destroy', 'update'] and (request.user == obj or request.user.is_superuser):
            return True
        else:
            return False
