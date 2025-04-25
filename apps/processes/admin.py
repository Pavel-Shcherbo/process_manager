from django.contrib import admin
from apps.core.mixins import CompanyScopedAdminMixin
from .models import Process, ProcessRelation

class ProcessRelationInline(admin.TabularInline):
    model = ProcessRelation
    fk_name = 'process'
    extra = 1

@admin.register(Process)
class ProcessAdmin(admin.ModelAdmin, CompanyScopedAdminMixin):
    list_display = ('id', 'branch', 'name', 'level', 'responsible')
    list_filter = ('branch',)
    inlines = [ProcessRelationInline]
    search_fields = ('name',)