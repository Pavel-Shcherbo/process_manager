from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Process, ProcessRelation
import json

@login_required
def process_tree_page(request):
    # Fetch all processes for user's scope
    if request.user.is_superuser:
        qs = Process.objects.all()
    elif request.user.role == 'ADMIN':
        qs = Process.objects.filter(branch=request.user.branch.company.processes__branch__company=request.user.branch.company)
    else:
        qs = Process.objects.filter(branch=request.user.branch)

    # Build nodes for jsTree
    nodes = []
    for p in qs:
        parent_ids = [rel.process_id for rel in ProcessRelation.objects.filter(sub_process=p)]
        nodes.append({
            'id': p.id,
            'parent': parent_ids[0] if parent_ids else '#',
            'text': p.name
        })

    return render(request, 'processes/tree.html', {
        'tree_data': json.dumps(nodes)
    })