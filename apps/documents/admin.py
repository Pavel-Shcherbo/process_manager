
from django.contrib import admin
from .models import Document

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'title', 'doc_type', 'process', 'signed_at')
    list_filter = ('doc_type', 'process__branch__company')
    search_fields = ('number', 'title')
