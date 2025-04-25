
from django.contrib import admin
from .models import Process, ProcessRelation

class ProcessRelationInline(admin.TabularInline):
    model = ProcessRelation
    fk_name = 'process'
    extra = 1

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin):
    list_display = ('id', 'branch', 'name', 'level')
    list_filter = ('branch',)
    search_fields = ('name',)
    inlines = [ProcessRelationInline]
