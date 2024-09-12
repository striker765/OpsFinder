from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_jobs, name='search_jobs'),
    path('show_all_servers/', views.show_all_servers, name='show_all_servers'),
    path('show_all_jobs/', views.show_all_jobs, name='show_all_jobs'),

]
