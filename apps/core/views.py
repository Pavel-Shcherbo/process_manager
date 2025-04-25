# apps/core/views.py
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.core.management import call_command
from pathlib import Path
from django.conf import settings

# ★ ДОБАВИТЬ ЭТИ ИМПОРТЫ
from apps.companies.models import Company
from apps.branches.models  import Branch
from apps.processes.models import Process
from apps.documents.models import Document


@login_required
def dashboard(request):
    qs_docs = Document.objects.all()
    if request.user.role == 'ADMIN':
        qs_docs = qs_docs.filter(process__branch__company=request.user.branch.company)
    elif request.user.role == 'USER':
        qs_docs = qs_docs.filter(process__branch=request.user.branch)

    kpis = [
        {"label":"Компаний",   "value":Company.objects.count(),                 "color":"primary"},
        {"label":"Филиалов",   "value":Branch.objects.count(),                 "color":"success"},
        {"label":"Процессов",  "value":Process.objects.count(),                "color":"warning"},
        {"label":"Документов", "value":qs_docs.count(),                        "color":"info"},
    ]
    return render(request, 'core/dashboard.html', {'kpis':kpis})

@login_required
def analytics_data(request):
    qs = Document.objects.values('process__name') \
            .annotate(total=Count('id')).order_by('-total')[:10]
    return JsonResponse({
        "labels":[x['process__name'] for x in qs],
        "data":[x['total'] for x in qs],
    })

from django.core.management import call_command, CommandError

@login_required
def generate_report(request):
    try:
        call_command('run_analysis')
    except CommandError:
        return HttpResponse("Команда run_analysis не найдена", status=500)
    path = Path(settings.MEDIA_ROOT, 'reports', 'report.xlsx')
    return FileResponse(open(path, 'rb'), as_attachment=True,
                        filename='documents_report.xlsx')
