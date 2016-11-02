# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import ListView

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
        form_with_blog = Post()
        posible_blog = Blog.objects.filter(owner=request.user)
        blog = posible_blog[0] if len(posible_blog) == 1 else None
        if blog is not None:
            form_with_blog.blog = blog
            form = PostForm(request.POST, instance=form_with_blog)
            new_post = form.save()
            form = PostForm()
            success_message = 'Guardado con éxito!'
            #success_message += '<a href="{0}">'.format(reverse('detail_post', args=[new_post.pk]))
            #success_message += 'Ver post'
            #success_message += '</a>'
        else:
            form = PostForm()
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