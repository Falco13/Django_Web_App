from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['theme', 'get_photo', 'active', 'create_date', 'update_date', 'user']
    search_fields = ['theme', 'active', 'create_date', 'user']
    list_filter = ['theme', 'active', 'create_date', 'update_date', 'user']
    list_editable = ['active']

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="75">')
        else:
            return '---'

    get_photo.short_description = 'Фото'


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'user', 'create_date', 'active']
    list_filter = ['user', 'create_date', 'active']
    list_editable = ['active']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'bio', 'date_of_birth', 'is_superuser']
    list_filter = ['username', 'first_name', 'last_name', 'email', 'date_of_birth']
    search_fields = ['username', 'first_name', 'last_name', 'email']
