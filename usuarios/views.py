from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib import auth


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home/')  
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'usuarios/login.html')

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout efetuado com sucess!')
    return redirect('login')


