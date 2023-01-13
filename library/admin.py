from django.contrib import admin
from .models import Set
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Set)
class SetAdmin(SummernoteModelAdmin):
    list_display = ('theme', 'pcs', 'set_number', 'is_built')
    search_fields = ['theme', 'pcs', 'set_number']
    summernote_fields = ('description')
