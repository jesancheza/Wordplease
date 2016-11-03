from django.contrib import admin
from posts.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    search_fields = ('category__title', )
    list_display = ('title', 'image_url', 'summary', 'date_published')
    ordering = ('-date_published',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_description')

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
