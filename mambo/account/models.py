#encoding:utf-8
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager

class UserProfileManager(BaseUserManager):
    
    def create_user(self, user, password, genero, nombre, apellidos, tipoDoc, numeroDoc, nacimiento, email):
        if not user:
            raise ValueError('Debe tener user')
        
        if not genero:
            raise ValueError('Debe tener genero ')

        if not nombre:
            raise ValueError('Debe tener nombre')
        
        if not apellidos:
            raise ValueError('Debe tener apellidos')
        
        if not tipoDoc:
            raise ValueError('Debe tener tipoDoc')
        
        if not numeroDoc:
            raise ValueError('Debe tener numeroDoc')
        
        if not nacimiento:
            raise ValueError('Debe tener tipoDoc')
        
        if not email:
            raise ValueError('Debe tener email')
        
        user = self.model(
            email=email,
            genero=genero,
            nombre=nombre,
            user=user,
            apellidos=apellidos,
            tipoDoc=tipoDoc,
            numeroDoc=numeroDoc,
            nacimiento=nacimiento
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,  user, password, genero, nombre, apellidos, tipoDoc, numeroDoc, nacimiento, email):
        user = self.create_user(user, password, genero, nombre, apellidos, tipoDoc, numeroDoc, nacimiento, email)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
        uuid        = models.AutoField(max_length=300, primary_key=True)
        user        = models.CharField(max_length=40, blank=True, unique=True)
        genero      = models.CharField(max_length=40, blank=True)
        nombre      = models.CharField(max_length=40, blank=True)
        apellidos   = models.CharField(max_length=100, blank=True)
        tipoDoc     = models.CharField(max_length=3, blank=True)
        numeroDoc   = models.CharField(max_length=40, blank=True)
        nacimiento  = models.CharField(max_length=40, blank=True)
        email       = models.EmailField(max_length=255, unique=True, db_index=True)
        foto        = models.ImageField(upload_to='perfiles',blank=True)
        USERNAME_FIELD  = 'user'
        REQUIRED_FIELDS = ['genero','nombre','apellidos','tipoDoc','numeroDoc','email','nacimiento']
        
        is_active = models.BooleanField(default=True)
        is_admin = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)
        
        objects = UserProfileManager()
        
        def get_full_name(self):
            return "Get_full_name: " + self.apellidos + self.nombre
        
        def get_short_name(self):
            return self.email
    
        def __unicode__(self):
            return self.user
    
# Habrá que agregarle un TIMESTAMP
class transport(models.Model):
        uuid        = models.ForeignKey(settings.AUTH_USER_MODEL)
        salida      = models.CharField(max_length=100)
        llegada     = models.CharField(max_length=100)
        fechasal    = models.CharField(max_length=100)
        fecharet    = models.CharField(max_length=100)
        plazas      = models.IntegerField(max_length=2)
    
        def __unicode__(self):
            return self.user
        
        