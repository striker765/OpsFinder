from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_jobs, name='search_jobs'),
]
