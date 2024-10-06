from django.urls import path
from . import views
from django.urls import path
from django.shortcuts import render



urlpatterns = [
    path('', views.search_jobs, name='search_jobs'),
    path('all_servers/', views.show_all_servers, name='all_servers'),
    path('all_FastShop/', views.show_all_fastshop, name='all_FastShop'),
    path('ajuda/', views.ajuda, name='ajuda'),
    path('all_jobs/', views.show_all_jobs, name='all_jobs'),

]



