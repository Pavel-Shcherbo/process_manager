from django.urls import path
from .views import DocumentListView, DocumentDetailView, DocumentCreateView

app_name = 'documents'
urlpatterns = [
    path('',          DocumentListView.as_view(),  name='list'),
    path('add/',      DocumentCreateView.as_view(), name='add'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='detail'),
]
