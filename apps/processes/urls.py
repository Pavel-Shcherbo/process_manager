from django.urls import path
from . import views

app_name = 'processes'
urlpatterns = [
    path('', views.process_tree_page, name='tree'),
]