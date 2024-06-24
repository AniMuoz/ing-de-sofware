from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,User

class UsuarioManager(BaseUserManager):
    def create_user(self, nombre_usuario, correo, tipo_cuenta, password=None, rut=None, rut_personal=None):
        if not nombre_usuario:
            raise ValueError("El usuario debe tener un nombre de usuario")
        if not correo:
            raise ValueError("El usuario debe tener un correo electrónico")
        if not rut:
            raise ValueError("El usuario debe tener un RUT")
        if not rut_personal:
            raise ValueError("El usuario debe tener un RUT personal")

        user = self.model(
            nombre_usuario=nombre_usuario,
            correo=self.normalize_email(correo),
            tipo_cuenta=tipo_cuenta,
            rut=rut,
            rut_personal=rut_personal,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, nombre_usuario, correo, tipo_cuenta, password=None, rut=None, rut_personal=None):
        user = self.create_user(
            nombre_usuario=nombre_usuario,
            correo=correo,
            password=password,
            tipo_cuenta=tipo_cuenta,
            rut=rut,
            rut_personal=rut_personal,
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
    rut = models.CharField(max_length=12, unique=True)
    rut_personal = models.CharField(max_length=12, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'nombre_usuario'
    REQUIRED_FIELDS = ['correo', 'tipo_cuenta', 'rut', 'rut_personal']

    def __str__(self):
        return self.nombre_usuario
