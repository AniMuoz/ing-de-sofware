# views.py
from django.shortcuts import render, redirect, render
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistroForm, IniciarSesionForm, RegistrationForm

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('iniciar_sesion')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def iniciar_sesion(request):
    if request.method == 'POST':
        form = IniciarSesionForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('inicio')
            else:
                return HttpResponse('Credenciales incorrectas, por favor intente de nuevo.')
    else:
        form = IniciarSesionForm()
    return render(request, 'iniciar_sesion.html', {'form': form})

def inicio(request):
    return render(request, 'inicio.html')

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, email=email, password=password)
            if user:
                return redirect('registration_success', username=username)
        else:
            return HttpResponse('Error en el formulario de registro')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def registration_success(request, username):
    return render(request, 'registration_success.html', {'username': username})

def logout_view(request):
    logout(request)
    return redirect('inicio')
def user_dashboard(request):
    # Asegúrate de que el usuario esté autenticado
    if not request.user.is_authenticated:
        return redirect('iniciar_sesion')
    
    # Lógica para tu dashboard
    return render(request, 'user_dashboard.html', {})

def profile_view(request):
    return render(request, 'profile.html')