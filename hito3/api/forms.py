from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class RegistroForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']
        # Verifica si el nombre de usuario ya existe en la base de datos
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username

class IniciarSesionForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())
    def clean_username(self):
        username = self.cleaned_data['username']
        # Verifica si el nombre de usuario ya existe en la base de datos
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return username
    
class SecondRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    rut = forms.CharField(max_length=12)
    rut_personal = forms.CharField(max_length=12)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'rut', 'rut_personal']

class SecondLoginForm(forms.Form):
    rut = forms.CharField(max_length=12)
    rut_personal = forms.CharField(max_length=12)
    password = forms.CharField(widget=forms.PasswordInput)