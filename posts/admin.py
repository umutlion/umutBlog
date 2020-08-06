from django.contrib import admin
from .models import Post, PostImage, Category, Comment
from django.db import models
# Register your models here.


class PostImageAdmin(admin.StackedInline):
    model = PostImage
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model=Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Comment)