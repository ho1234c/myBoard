from django.contrib import admin
from .models import *
# Register your models here.


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created')


class PostsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'content', 'created')

admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Comments, CommentsAdmin)
admin.site.register(Posts, PostsAdmin)
admin.site.register(Users, UsersAdmin)
