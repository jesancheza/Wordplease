# -*- coding: utf-8 -*-
from django.db.models import Q
from django.shortcuts import render
from django.utils.datetime_safe import datetime
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView, View

from posts.models import Post, PUBLIC
from blogs.models import Blog
from posts.forms import PostForm
from django.contrib.auth.decorators import login_required


class PostQueryset(object):

    def get_post_queryset(self, request):

        today = datetime.now()
        if not request.user.is_authenticated():
            post = Post.objects.filter(date_published__lte=today, type=PUBLIC).order_by('-date_published')
        elif request.user.is_superuser:
            post = Post.objects.all().order_by('-date_published')
        else:
            post = Post.objects.filter(Q(date_published__lte=today, type=PUBLIC) | Q(blog__owner=request.user))\
                .order_by('-date_published')

        return post


class HomeView(PostQueryset, ListView):

    """
    Muestra la pantalla home con los últimos post creados
    """
    model = Post
    template_name = 'posts/home.html'
    ordering = '-date_published'
    paginate_by = 5

    def get_queryset(self):
        return self.get_post_queryset(self.request).select_related('blog')


class PostCreateView(View):

    @method_decorator(login_required)
    def get(self, request):
        """
        Muestra un formulario para crear un nuevo post.
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''
        form = PostForm()

        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'posts/new_post.html', context)

    @method_decorator(login_required)
    def post(self, request):
        """
        Muestra un formulario para crear un nuevo post.
        :param request: HttpRequest
        :return: HttpResponse
        """
        success_message = ''

        form_with_blog = Post()
        posible_blog = Blog.objects.filter(owner=request.user)
        blog = posible_blog[0] if len(posible_blog) == 1 else None
        if blog is not None:
            form_with_blog.blog = blog
            form = PostForm(request.POST, instance=form_with_blog)
            if form.is_valid():
                new_post = form.save()
                form = PostForm()
                success_message = 'Guardado con éxito!'
        else:
            form = PostForm()
        context = {
            'form': form,
            'success_message': success_message
        }

        return render(request, 'posts/new_post.html', context)


class PostDetailView(PostQueryset, DetailView):
    model = Post
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        return self.get_post_queryset(self.request)
