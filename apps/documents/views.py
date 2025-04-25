# apps/documents/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from apps.core.mixins import BranchScopedMixin
from .models import Document
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Document
from .forms import DocumentForm
class DocumentListView(LoginRequiredMixin, BranchScopedMixin, ListView):
    model = Document
    template_name = 'documents/list.html'
    paginate_by = 25


class DocumentDetailView(LoginRequiredMixin, BranchScopedMixin, DetailView):
    model = Document
    template_name = 'documents/detail.html'


class DocumentCreateView(LoginRequiredMixin, BranchScopedMixin, CreateView):
    model         = Document
    form_class    = DocumentForm
    template_name = 'documents/form.html'
    success_url   = reverse_lazy('documents:list')

    def form_valid(self, form):
        # ADMIN может привязать к любому процессу своей компании,
        # USER — только к процессам своего филиала
        return super().form_valid(form)
