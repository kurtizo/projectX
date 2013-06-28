from django.db import models
from django.contrib.auth.models import ( BaseUserManager, AbstractBaseUser, PermissionsMixin )

class MamboUserManager(BaseUserManager): 
    def create_user(self, user, date_of_birth, password=None): 
        if not email: 
            raise ValueError('Users must have an email address') 

        user = self.model( 
            user=user, 
            date_of_birth=date_of_birth, 
        ) 

        user.set_password(password) 
        user.save(using=self._db) 
        return user 

    def create_superuser(self, username, password, date_of_birth): 
        u = self.create_user(username, password=password, date_of_birth=date_of_birth) 
        u.is_admin = True 
        u.save(using=self._db) 
        return u
    
class UserProfile(AbstractBaseUser):
    user        = models.CharField(max_length=40, unique=True, db_index=True)
    genero      = models.CharField(max_length=40, blank=True)
    nombre      = models.CharField(max_length=40, blank=True)
    apellidos   = models.CharField(max_length=100, blank=True)
    tipoDoc     = models.CharField(max_length=3, blank=True)
    numeroDoc   = models.CharField(max_length=40, blank=True)
    nacimiento  = models.CharField(max_length=40, blank=True)
    email       = models.EmailField(max_length=255, unique=True, db_index=True)
    USERNAME_FIELD  = 'user'
    REQUIRED_FIELDS = ['genero','nombre','apellidos','tipoDoc','numeroDoc','email','nacimiento']

    def get_full_name(self):
        return self.user
 
    def get_short_name(self):
        return self.user
 
    def __unicode__(self):
        return self.user
 
    def has_perm(self, perm, obj=None):
        return True
 
    def has_module_perms(self, app_label):
        return True
 
    @property
    def is_staff(self):
        return self.is_admin
