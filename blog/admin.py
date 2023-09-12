"""blog.admin."""
from adminfilters.autocomplete import AutoCompleteFilter
from adminfilters.combo import ChoicesFieldComboFilter
from adminfilters.dj import DjangoLookupFilter
from adminfilters.json import JsonFieldFilter
from adminfilters.numbers import NumberFilter
from adminfilters.querystring import QueryStringFilter
from adminfilters.value import ValueFilter
from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.forms import JSONField

from . import models
from .models import Post,  Comments
class CommentInline(admin.TabularInline):
    model = Comments
    extra = 0

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """."""
    list_display = ("title", "author", "category")
    fields = ("title", "author", "text", "category", "published_date")
    inlines = [CommentInline]




class FilterDepotManager:
    pass

