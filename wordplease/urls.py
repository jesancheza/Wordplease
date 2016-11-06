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

from blogs import urls as blog_urls, api_urls as blog_api_urls
from posts import urls as post_urls, api_urls as post_api_urls
from users import urls as user_urls, api_urls as user_api_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include(blog_urls)),
    url(r'', include(post_urls)),
    url(r'', include(user_urls)),

    url(r'', include(blog_api_urls)),
    url(r'', include(post_api_urls)),
    url(r'', include(user_api_urls)),
]
