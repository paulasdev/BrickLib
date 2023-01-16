from django.contrib import admin
from .models import Set
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Set)
class SetAdmin(admin.ModelAdmin):
    list_display = ('theme', 'title', 'description', 'done')
    search_fields = ('theme', 'title', 'description')
    # summernote_fields = ('description')
