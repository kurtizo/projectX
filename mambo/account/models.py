#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    uuid        = models.ForeignKey(User, unique=True)
    user        = models.CharField(max_length=40, blank=True, primary_key=True)
    genero      = models.CharField(max_length=40, blank=True)
    nombre      = models.CharField(max_length=40, blank=True)
    apellidos   = models.CharField(max_length=100, blank=True)
    tipoDoc     = models.CharField(max_length=3, blank=True)
    numeroDoc   = models.CharField(max_length=40, blank=True)
    nacimiento  = models.CharField(max_length=40, blank=True)
    email       = models.EmailField(max_length=255, unique=True, db_index=True)
    foto        = models.ImageField(upload_to='perfiles',blank=True)
    
    def __unicode__(self):
        return self.user

class transport(models.Model):
    uuid        = models.ForeignKey(User)
    salida      = models.CharField(max_length=100)
    llegada     = models.CharField(max_length=100)
    fecha       = models.DateField(("Date"))
    horario     = models.DateField(("Hora"))
    plazas      = models.IntegerField(max_length=2)

    def __unicode__(self):
        return self.user