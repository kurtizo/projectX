from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user        = models.ForeignKey(User.username)
    genero      = models.CharField(max_length=40, blank=True)
    nombre      = models.CharField(max_length=40, blank=True)
    apellidos   = models.CharField(max_length=100, blank=True)
    tipoDoc     = models.CharField(max_length=3, blank=True)
    numeroDoc   = models.CharField(max_length=40, blank=True)
    nacimiento  = models.CharField(max_length=40, blank=True)
    email       = models.EmailField(max_length=255, unique=True, db_index=True)
    foto        = models.ImageField(upload_to='perfiles',blank=True)
