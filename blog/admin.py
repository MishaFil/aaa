"""blog.admin."""
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """."""
    list_display = ("title", "author")
    fields = ("title", "author", "text")

    # inlines = []
