# dashboard/urls.py
from django.urls import path
from .views import dashboard_view
from .views import get_log_data
from django.conf import settings
urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('log_data/', get_log_data, name='log_data'),
    
]
