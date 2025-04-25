from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from apps.core.mixins import CompanyScopedAdminMixin
from apps.companies.models import Company
from apps.branches.models import Branch
from apps.processes.models import Process, ProcessRelation
from apps.documents.models import Document
from apps.users.models import User

class StaffSite(admin.AdminSite):
    site_header = "Process Manager — Staff"
    site_title = "Staff"

    def has_permission(self, request):
        return request.user.is_active and request.user.role in ('ADMIN', 'SUPERADMIN')

staff_site = StaffSite(name='staff')

# Register models with proper permissions and changelist link fixes
@admin.register(Company, site=staff_site)
class CompanyAdmin(CompanyScopedAdminMixin):
    list_display = ('id', 'name', 'short_name')
    search_fields = ('name',)

@admin.register(Branch, site=staff_site)
class BranchAdmin(CompanyScopedAdminMixin):
    list_display = ('id', 'company', 'name')
    list_filter = ('company',)

class ProcessRelationInline(admin.TabularInline):
    model = ProcessRelation
    fk_name = 'process'
    extra = 1

@admin.register(Process, site=staff_site)
class ProcessAdmin(CompanyScopedAdminMixin):
    list_display = ('id', 'branch', 'name', 'level', 'responsible', 'document_count')
    list_filter = ('branch',)
    inlines = [ProcessRelationInline]

    def document_count(self, obj):
        # Use known URL name for Document changelist in staff site
        url = reverse('staff:documents_document_changelist') + f'?process__id__exact={obj.id}'
        return format_html("<a href='{}'>{}</a>", url, obj.documents.count())
    document_count.short_description = "Документов"

@admin.register(Document, site=staff_site)
class DocumentAdmin(CompanyScopedAdminMixin):
    list_display = ('id', 'number', 'title', 'doc_type', 'process', 'signed_at')
    list_filter = ('doc_type', 'process__branch__company')

@admin.register(User, site=staff_site)
class UserAdmin(CompanyScopedAdminMixin):
    list_display = ('username', 'email', 'role', 'branch', 'is_active')
    list_filter = ('role', 'is_active')
    search_fields = ('username', 'email')
    fieldsets = (
        ('Основное', {'fields': ('username', 'password', 'role', 'is_active')}),
        ('Личные данные', {'fields': ('full_name', 'email', 'phone')}),
        ('Компания/Филиал', {'fields': ('branch', 'position', 'department')}),
    )