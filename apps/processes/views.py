
from django.shortcuts import render, get_object_or_404
from .models import Process, ProcessRelation
from types import SimpleNamespace


def process_list(request):
    processes = Process.objects.select_related('branch').all()
    return render(request, 'processes/list.html', {'processes': processes})

def build_tree(node):
    return SimpleNamespace(
        process=node,
        children=[
            build_tree(rel.sub_process)
            for rel in node.children_rel.select_related('sub_process')
        ]
    )

def process_detail(request, pk):
    process = get_object_or_404(Process, pk=pk)
    tree = build_tree(process)
    return render(request, 'processes/detail.html', {'tree': tree})
