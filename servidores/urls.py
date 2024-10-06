from django.urls import path
from . import views
from .views import dashboard_view  # Corrigido para importar a view correta

urlpatterns = [
    path('show_all_servers/', views.show_all_servers, name='show_all_servers'),
]
