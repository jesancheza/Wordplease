from django.contrib import admin
from blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner')
    ordering = ('-created_at', )

admin.site.register(Blog, BlogAdmin)
