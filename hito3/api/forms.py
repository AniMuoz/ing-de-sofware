from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Usuario

class RegistroForm(UserCreationForm):
    rut = forms.CharField(max_length=12, required=True)
    rut_personal = forms.CharField(max_length=12, required=True)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'correo', 'rut', 'rut_personal', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.correo = self.cleaned_data['correo']
        if commit:
            user.save()
        return user

    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data['nombre_usuario']
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return nombre_usuario

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if Usuario.objects.filter(rut=rut).exists():
            raise forms.ValidationError("Este RUT ya está en uso.")
        return rut

    def clean_rut_personal(self):
        rut_personal = self.cleaned_data['rut_personal']
        if Usuario.objects.filter(rut_personal=rut_personal).exists():
            raise forms.ValidationError("Este RUT personal ya está en uso.")
        return rut_personal

class IniciarSesionForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

class IniciarSesionForm(AuthenticationForm):
    username = forms.CharField(label='Nombre de usuario')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())

class SecondLoginForm(forms.Form):
    rut = forms.CharField(max_length=12, required=True)
    rut_personal = forms.CharField(max_length=12, required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class SecondRegistrationForm(UserCreationForm):
    rut = forms.CharField(max_length=12, required=True)
    rut_personal = forms.CharField(max_length=12, required=True)

    class Meta:
        model = Usuario
        fields = ('nombre_usuario', 'correo', 'rut', 'rut_personal', 'password1', 'password2')

    def clean_nombre_usuario(self):
        nombre_usuario = self.cleaned_data['nombre_usuario']
        if Usuario.objects.filter(nombre_usuario=nombre_usuario).exists():
            raise forms.ValidationError("Este nombre de usuario ya está en uso.")
        return nombre_usuario

    def clean_rut(self):
        rut = self.cleaned_data['rut']
        if Usuario.objects.filter(rut=rut).exists():
            raise forms.ValidationError("Este RUT ya está en uso.")
        return rut

    def clean_rut_personal(self):
        rut_personal = self.cleaned_data['rut_personal']
        if Usuario.objects.filter(rut_personal=rut_personal).exists():
            raise forms.ValidationError("Este RUT personal ya está en uso.")
        return rut_personal


class RegistrationForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Correo electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput())