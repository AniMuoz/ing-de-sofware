from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.models import User
from .forms import RegistroForm, IniciarSesionForm,   SecondLoginForm, SecondRegistrationForm,RegistrationForm
from .models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .forms import RegistroForm, IniciarSesionForm

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
    return render(request, 'registre.html', {'form': form})

def registration_success(request, username):
    return render(request, 'registre.html', {'username': username})


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





def logout_view(request):
    logout(request)
    return redirect('inicio')

def user_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('iniciar_sesion')
    return render(request, 'user_dashboard.html', {})

def profile_view(request):
    return render(request, 'profile.html')


def second_login_view(request):
    if request.method == 'POST':
        form = SecondLoginForm(request.POST)
        if form.is_valid():
            rut = form.cleaned_data['rut']
            rut_personal = form.cleaned_data['rut_personal']
            password = form.cleaned_data['password']
            user = authenticate(request, rut=rut, rut_personal=rut_personal, password=password)
            if user is not None:
                login(request, user)
                return redirect('wz.html')  # or wherever you want to redirect
            else:
                form.add_error(None, "Credenciales inválidas")
    else:
        form = SecondLoginForm()
    return render(request, 'login_empresa.html', {'form': form})

def second_registration_view(request):
    if request.method == 'POST':
        form = SecondRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')  # Redirige al usuario a la página de inicio de sesión después del registro exitoso
    else:
        form = SecondRegistrationForm()
    return render(request, 'second_registration.html', {'form': form})


def second_dashboard(request):
    if not request.user.is_authenticated:
        return redirect('login_empresa')
    return render(request, 'second_dashboard.html')

def registration_empresa_success(request, username):
    return render(request, 'registration_success.html', {'username': username})

def Carrito_view(request):
    return render(request, 'carrito.html')



def fabian_view(request):
    return render(request, 'fabian.html')
def gg(request):
    return render(request, 'gg.html')

def pagar_view(request):
    return render(request,'pagar.html' )


def compra_view(request):
    return render(request, 'compra.html')

def ver_view(request):
    return render(request, 'ver.html') 


def compraz_view(request):
    return render(request, 'compraz.html')

def test1_view(request):
    return render(request, 'test1.html')
def test2_view(request):
    return render(request, 'test2.html')

def test2_view(request):
    return render(request, 'test2.html')
def a_view(request):
    return render(request, 'a.html')
def b_view(request):
    return render(request, 'b.html')


def c_view(request):
    return render(request, 'c.html')


def d_view(request):
    return render(request, 'd.html')

def e_view(request):
    return render(request, 'e.html')
def test3_view(request):
    return render(request, 'test3.html')


def test4_view(request):
    return render(request, 'test4.html')


def test5_view(request):
    return render(request, 'test5.html')


def test6_view(request):
    return render(request, 'test6.html')


def test7_view(request):
    return render(request, 'test7.html')


def test8_view(request):
    return render(request, 'test8.html')


def test9_view(request):
    return render(request, 'test9.html')


def test10_view(request):
    return render(request, 'test10.html')


def test11_view(request):
    return render(request, 'test11.html')


def test12_view(request):
    return render(request, 'test12.html')

def test13_view(request):
    return render(request, 'test13.html')
def test14_view(request):
    return render(request, 'test14.html')


def chat(request):
    return render(request, 'chat.html')


def procesos(request):
    return render(request, 'procesos.html')

def wz(request):
    return render(request, 'wz.html')