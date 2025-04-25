from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    path('', views.dashboard,         name='dashboard'),
    path('analytics-data/', views.analytics_data, name='analytics_data'),
    path('generate-report/', views.generate_report, name='generate_report'),
]
