from django.contrib import admin
from django.core.exceptions import PermissionDenied

class CompanyScopedAdminMixin(admin.ModelAdmin):
    """
    Ограничивает ADMIN-у доступ рамками своей компании,
    SUPERADMIN видит всё. Плюс выдаём «view / change» права,
    чтобы разделы отображались в StaffSite.
    """
    # -------- queryset ----------
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        u  = request.user
        if u.is_superuser:
            return qs
        if u.role == 'ADMIN' and u.branch:
            return qs.filter(company=u.branch.company)
        return qs.none()

    # -------- права на объекты ----------
    def has_view_permission(self, request, obj=None):
        if obj and request.user.role == 'ADMIN':
            try:
                company = getattr(obj, "company", None) or obj.branch.company
            except AttributeError:
                return False
            return company == request.user.branch.company
        return super().has_view_permission(request, obj)

    # -------- меню и кнопки ----------
    def get_model_perms(self, request):
        """
        Django рисует пункт меню только если хоть одно из perms=True.
        Дадим ADMIN-у полный набор CRUD-прав внутри StaffSite.
        """
        perms = super().get_model_perms(request)
        if request.user.role == 'ADMIN':
            return {k: True for k in ('add', 'change', 'delete', 'view')}
        return perms

    def has_module_permission(self, request):
        # Пункт меню показываем ADMIN-у всегда, даже если объектов ноль
        if request.user.role == 'ADMIN':
            return True
        return super().has_module_permission(request)


class BranchScopedMixin:
    """USER → свой филиал, ADMIN → компания, SUPERADMIN → всё."""
    def get_queryset(self):
        qs = super().get_queryset()
        u  = self.request.user

        if u.is_superuser:
            return qs

        # Определяем тип модели (Document имеет связь process→branch)
        is_document = qs.model._meta.model_name == 'document'

        if u.role == 'ADMIN' and u.branch:
            company = u.branch.company
            return qs.filter(
                process__branch__company=company if is_document else
                {'branch__company': company} [not is_document]  # трюк выбора
            )

        if u.role == 'USER' and u.branch:
            branch = u.branch
            return qs.filter(
                process__branch=branch if is_document else
                {'branch': branch} [not is_document]
            )

        return qs.none()
