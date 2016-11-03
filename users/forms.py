# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

__author__ = 'jesanchez'


class LoginForm(forms.Form):
    """
    Formulario para el login
    """
    usr = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(ModelForm):
    """
    Formulario para el alta de usuarios
    """

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', ]:
            self.fields[fieldname].help_text = None

        for fieldname in ['username', 'email', 'password']:
            self.fields[fieldname].required = True
