from django.urls import path
from . import views
from django.urls import path
from django.shortcuts import render



urlpatterns = [
    path('', views.search_jobs, name='search_jobs'),
    path('show_all_servers/', views.show_all_servers, name='show_all_servers'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('show_all_jobs/', views.show_all_jobs, name='show_all_jobs'),

]



