from django.contrib import admin
from .models import Post, comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'title', 'slug', 'author', 'created'
    list_display_links = 'title', 'slug'
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']

@admin.register(comment)
class commentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email' , 'post', 'created', 'active']
    list_display_links = ['name']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'body']
