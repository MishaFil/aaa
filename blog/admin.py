"""blog.admin."""
from django.contrib import admin
from .models import Post,Category

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """."""
    list_display = ("title", "author","category")
    fields = ("title", "author", "text","category")


