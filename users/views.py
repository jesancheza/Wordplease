# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout, authenticate, login as django_login

from blogs.models import Blog
from users.forms import LoginForm, SignupForm
from django.views.generic import View


class LoginView(View):

    def get(self, request):
        error_messages = []
        form = LoginForm()
        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)

    def post(self, request):
        error_messages = []
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_messages.append('Nombre de usuario o contraseña incorrectos.')
            else:
                if user.is_active:
                    django_login(request, user)
                    url = request.GET.get('next', 'wordplease_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo')

        context = {
            'errors': error_messages,
            'login_form': form
        }
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('wordplease_home')


class SignupView(View):

    def get(self, request):
        form = SignupForm()
        context = {
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)

    def post(self, request):
        error_messages = []
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('usr')
            password = form.cleaned_data.get('pwd')
            email = form.cleaned_data.get('email')

            user = User.objects.filter(email=email)
            if user.exists():
                error_messages.append('Ya existe un usuario con este email')
            else:
                # creamos el usuario
                new_user = form.save()
                new_user.set_password(new_user.password)
                new_user.save()
                form = SignupForm()

                if new_user.is_active:
                    # nos autenticamos
                    user = authenticate(username=new_user.username, password=new_user.password)

                    # creamos el blog del usuario
                    blog = Blog(owner=new_user)
                    blog.title = 'Blog de ' + new_user.username
                    blog.save()

                    # redireccionamos a la página de inicio
                    django_login(request, user)
                    url = request.GET.get('next', 'wordplease_home')
                    return redirect(url)
                else:
                    error_messages.append('El usuario no está activo, contacte con el administrador del sitio.')

        context = {
            'errors': error_messages,
            'signup_form': form
        }
        return render(request, 'users/signup.html', context)
