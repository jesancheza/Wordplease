# -*- coding: utf-8 -*-
from django.shortcuts import render
from posts.models import Post
from posts.forms import PostForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseNotFound
from django.contrib.auth.decorators import login_required

def home(request):
    """
    Muestra la pantalla home con los ultimos post creados
    :param request: HttpRequest
    :return: HttpResponse
    """
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts[:5]
    }

    return render(request, 'posts/home.html', context)

@login_required()
def create(request):
    """
    Muestra un formulario para crear un nuevo post.
    :param request: HttpRequest
    :return: HttpResponse
    """
    success_message = ''
    if request.method == 'GET':
        form = PostForm()
    else:
        form = PostForm(request.POST)
        new_post = form.save()
        form = PostForm()
        success_message = 'Guardado con éxito!'
        success_message += '<a href="{0}">'.format(reverse('detail_post', args=[new_post.pk]))
        success_message += 'Ver post'
        success_message += '</a>'
    context = {
        'form': form,
        'success_message': success_message
    }

    return render(request, 'posts/new_post.html', context)

def detail(request, pk):
    posible_post = Post.objects.filter(pk=pk)
    post = posible_post[0] if len(posible_post) >= 1 else None
    if post is not None:
        context = {
            'post': post
        }
        return render(request, 'post_detail', context)
    else:
        return HttpResponseNotFound('No existe el post.')