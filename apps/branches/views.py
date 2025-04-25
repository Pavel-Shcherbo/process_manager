
from django.shortcuts import render
from .models import Branch

def branch_list(request):
    branches = Branch.objects.select_related('company')
    return render(request, 'branches/list.html', {'branches': branches})
