"""blog.admin."""
from django.contrib import admin
from .models import Post, Category, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """."""
    list_display = ("title", "author", "category")
    fields = ("title", "author", "text", "category", "published_date")


class CommentInline(admin.TabularInline):
    model = Comments
    extra = 0


inlines = [CommentInline]
