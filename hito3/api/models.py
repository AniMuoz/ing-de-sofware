from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User





class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, correo, tipo_cuenta, password=None):
        if not nombre_usuario:
            raise ValueError("El usuario debe tener un nombre de usuario")
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")

        user = self.model(
            nombre_usuario=nombre_usuario,
            correo=self.normalize_email(correo),
            tipo_cuenta=tipo_cuenta,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, correo, tipo_cuenta,password=None):
        user = self.create_user(
            nombre_usuario=nombre_usuario,
            correo=correo,
            password=password,
            tipo_cuenta=tipo_cuenta,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    TIPOS_CUENTA = (
        ('P', 'Persona'),
        ('E', 'Empresa'),
    )

    nombre_usuario = models.CharField(max_length=30, unique=True)
    correo = models.EmailField(unique=True)
   
    tipo_cuenta = models.CharField(max_length=1, choices=TIPOS_CUENTA)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre_usuario'
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12, unique=True)
    rut_personal = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.user.usernam


