# -*- coding: utf-8 -*-
from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from users.permissions import UserPermissions
from users.serializers import UserSerializer, UserDetailSerializer


class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (UserPermissions, )

    def get_serializer_class(self):

        if self.action == 'retrieve':
            return UserDetailSerializer
        else:
            return UserSerializer
