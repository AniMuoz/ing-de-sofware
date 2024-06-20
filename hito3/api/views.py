from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistroForm, IniciarSesionForm, RegistrationForm, SecondRegistrationForm, SecondLoginForm

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
    if not request.user.is_authenticated:
        return redirect('iniciar_sesion')
    return render(request, 'user_dashboard.html', {})

def profile_view(request):
    return render(request, 'profile.html')

def register_empresa(request):
    if request.method == 'POST':
        form = SecondRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            # Save additional fields to user's profile or a related model if needed
            user.profile.rut = form.cleaned_data['rut']
            user.profile.rut_personal = form.cleaned_data['rut_personal']
            user.profile.save()
            return redirect('login_empresa')
        else:
            return HttpResponse('Error en el formulario de registro')
    else:
        form = SecondRegistrationForm()
    return render(request, 'register_empresa.html', {'form': form})

def login_empresa(request):
    if request.method == 'POST':
        form = SecondLoginForm(data=request.POST)
        if form.is_valid():
            rut_personal=form.cleaned_data.get('rut_personal')
            rut = form.cleaned_data.get('rut')
            password = form.cleaned_data.get('password')
            try:
                user = User.objects.get(profile__rut=rut)
            except User.DoesNotExist:
                return HttpResponse('Credenciales incorrectas, por favor intente de nuevo.')
            user = authenticate(username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('second_dashboard')
            else:
                return HttpResponse('Credenciales incorrectas, por favor intente de nuevo.')
    else:
        form = SecondLoginForm()
    return render(request, 'login_empresa.html', {'form': form})

def second_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('second_login')
    return render(request, 'second_dashboard.html')
def registration_empresa_success(request, username):
    return render(request, 'registration_success.html', {'username': username})








def compra_view(request):
    return render(request, 'compra.html')


def compraz_view(request):
    return render(request, 'compraz.html')