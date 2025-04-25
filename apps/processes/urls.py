
from django.urls import path
from . import views
app_name = 'processes'
urlpatterns = [
    path('', views.process_list, name='list'),
    path('<int:pk>/', views.process_detail, name='detail'),
]
