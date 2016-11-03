# -*- coding: utf-8 -*-
from django import forms
from posts.models import Post

__author__ = 'jesanchez'


class PostForm(forms.ModelForm):
    """
    Formulario para el modelo Post
    """
    class Meta:
        model = Post
        exclude = ['blog']
