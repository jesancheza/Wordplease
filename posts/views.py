# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import ListView, View

from posts.models import Post
from blogs.models import Blog
from posts.forms import PostForm
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required


class HomeView(ListView):

    """
    Muestra la pantalla home con los últimos post creados
    """
    model = Post
    template_name = 'posts/home.html'
    queryset = Post.objects.all().select_related('blog')
    ordering = '-created_at'
    paginate_by = 5


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


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    """
    def get(self, request, username, pk):
        posible_post = Post.objects.filter(pk=pk)
        post = posible_post[0] if len(posible_post) >= 1 else None
        if post is not None:
            context = {
                'post': post
            }
            return render(request, 'posts/post_detail.html', context)
        else:
            return HttpResponseNotFound('No existe el post.')
    """