from django.contrib import admin
from django.utils.html import format_html
from post.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', '_clickable_photo', 'created_at', 'content']
    readonly_fields = ['id', '_clickable_photo', 'created_at']
    fields = ['id', 'user', '_clickable_photo', 'photo', 'created_at', 'content']

    def _clickable_photo(self, post:Post):
        html = '<a href="{link}"><img src="{photo}" width=100 height=100 /></a>'
        if post.photo:
            return format_html(html, link=post.photo.url, photo=post.photo.url)
        return format_html('<strong> _ <strong>')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post', 'created_at', 'content']
    readonly_fields = ['id', 'created_at']
    fields = ['id', 'user', 'created_at', 'content']

