from django.shortcuts import render
from posts.models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'posts': posts[:5]
    }

    return render(request, 'posts/home.html', context)