from django.urls import path
from .admin import staff_site
urlpatterns = [ path('', staff_site.urls) ]
