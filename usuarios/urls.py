from django.urls import path
from usuarios.views import login_view , logout

urlpatterns = [
    path('', login_view, name='login'), 
    path('logout', logout, name ='logout'),
]