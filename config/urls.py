from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/',    admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),     # страница логина
    path('',          include('apps.core.urls')),
    path('companies/', include('apps.companies.urls')),
    path('branches/',  include('apps.branches.urls')),
    path('processes/', include('apps.processes.urls')),
    path('documents/', include('apps.documents.urls')),         # ★ ОБЯЗАТЕЛЬНО
    path('staff/',     include('apps.staff.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
