from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('jobs.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('',include ('usuarios.urls')),
    
]