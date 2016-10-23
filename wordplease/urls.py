"""wordplease URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from users.views import LoginView, LogoutView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Blog UR   Ls
    url(r'^blogs$', 'blogs.views.home', name='blogs_home'),
    url(r'^blogs/(?P<username>[-\w]+)$', 'blogs.views.detail', name='detail_blog'),

    # Post URLs
    url(r'^$', 'posts.views.home', name='wordplease_home'),
    url(r'^blogs/(?P<username>[-\w]+)/(?P<pk>[0-9]+)$', 'posts.views.detail', name='post_detail'),
    url(r'^new-post$', 'posts.views.create', name='create_post'),

    # Users URLs
    url(r'^login$', LoginView.as_view(), name='users_login'),
    url(r'^logout$', LogoutView.as_view(), name='users_logout'),
]
