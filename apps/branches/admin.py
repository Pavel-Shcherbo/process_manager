
from django.contrib import admin
from .models import Branch

@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'company', 'name')
    list_filter = ('company',)
    search_fields = ('name',)
