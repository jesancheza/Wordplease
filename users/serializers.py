# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers

from blogs.models import Blog

__author__ = 'joseenriquesanchezalfonso'


class UserDetailSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class UserSerializer(serializers.ModelSerializer):

    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')

    def create(self, validated_data):
        """
        Crea un User a partir de validated_data (valores deserializados)
        """

        instance = User()
        user = self.update(instance, validated_data)
        if user:
            Blog.objects.create(owner=user, title='Blog de '+user.first_name)
        return user

    def update(self, instance, validated_data):
        """
        Actualiza uns instancia User a partir de los datos del diccionario
        validate_data que contiene datos deserializados
        """
        instance.first_name = validated_data.get('first_name')
        instance.last_name = validated_data.get('last_name')
        instance.username = validated_data.get('username')
        instance.set_password(validated_data.get('password'))
        instance.email = validated_data.get('email')
        instance.save()
        return instance

    def validate_username(self, data):
        """
        Validamos si existe un user con el mismo username
        """

        users = User.objects.filter(username=data)

        # caso CREATE (no hay instancia),  comprobamos si hay algún usuario con ese username
        if not self.instance and len(users) != 0:
            raise serializers.ValidationError('Ya existe un usuario con este username')
        else:
            return data
        # Si estoy actualizando y el nuevo username es diferente al de la instancia (está cambiando el username)
        # comprobamos si existen usuarios ya registrados con el nuevo username
        if self.instance.username != data and len(users) != 0:
            raise serializers.ValidationError('Ya existe un usuario con este username')
        else:
            return data
