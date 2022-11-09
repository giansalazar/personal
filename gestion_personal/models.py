from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser

# Create your models here.

class UsuarioManager(BaseUserManager):

    def _create_user(self, username, id_persona_id, telefono, email, is_active, is_staff, tipo_usuario, is_superuser, password):
        if not email:
            raise ValueError("El usuario debe tener un email")
        
        usuario = self.model(username=username, id_persona_id=id_persona_id, telefono=telefono, email=self.normalize_email(email), is_active=is_active, is_staff=is_staff, tipo_usuario=tipo_usuario, is_superuser=is_superuser)

        usuario.set_password(password)
        usuario.save(using=self.db)
        return usuario
    
    def create_user(self, username, id_persona_id, telefono, email, tipo_usuario, password=None):
        return self._create_user(username, id_persona_id, telefono, email, True, True, tipo_usuario, False, password)
    
    def create_superuser(self, username, id_persona_id, telefono, email, password):
        
        usuario=self.create_user(email,username=username, id_persona=id_persona_id, telefono=telefono, email=email, password=password)

        usuario.is_superuser=True

        usuario.save()

        return usuario
    

class Personas(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=30, verbose_name="Nombre")
    apep = models.CharField(max_length=30, verbose_name="Apellido Paterno")
    apem = models.CharField(max_length=30, verbose_name="Apellido Materno")
    genero = models.CharField(max_length=10)
    username = models.CharField(verbose_name="Usuario", max_length=20, unique=True)
    telefono =  models.CharField(max_length=10, verbose_name="Télefono")
    email = models.EmailField(verbose_name="Email")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    objects=UsuarioManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = 'telefono','email'

class Jefaturas(models.Model):
    nombre = models.CharField(max_length=30)

class Puestos(models.Model):
    nombre = models.CharField(max_length=30)
    id_jefatura = models.ForeignKey(Jefaturas, on_delete=models.CASCADE)

class Empleados(models.Model):
    id_persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    id_puesto = models.ForeignKey(Puestos, on_delete=models.CASCADE)
