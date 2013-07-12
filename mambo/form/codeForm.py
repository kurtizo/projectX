#encoding:utf-8
from django import forms
from django.contrib.admin import widgets 

GENERE_CHOICES = (
         ('hombre','Hombre'),
         ('mujer','Mujer'),
    )

TIPDOC_CHOICES = (
        ('NIF', 'NIF'),
        ('NIE', 'NIE'),
        ('passp', 'Pasaporte'),
    )

CITY_CHOICES = (
        ('leganes', 'CD Leganés'),
        ('Real Oviedo','Real Oviedo'),
        ('Mieres', 'Caudal Mieres'),
        ('Rmadrid', 'Real Madrid "C"'),
        ('Fuenlabrada', 'CF Fuenlabrada'),
        ('AtlMadrid', 'Atl Madrid "B"'),
        ('Salamanca', 'UD Salamanca'),
        ('Coruxo', 'Coruxo CF'),
        ('Getafe', 'Getafe CF "B"'),
        ('Luanco' , 'Marino Luanco'),
        ('Ourense', 'CD Ourense'),
        ('Aldeona', 'Sp. Gijón B'),
        ('Aviles', 'Real Avilés CF'),
        ('Guijuelo', 'CD Guijuelo'),
        ('Zamora', 'Zamora CF'),
        ('Sanse', 'UD S.Sebastián'),
        ('Alcala', 'RSD Alcalá'),
        ('Vallecas', 'Rayo Vallecano B'),
        ('Ferrol', 'Racing club de Ferrol'),
        ('Vigo', 'RC Celta de Vigo "B"'),
        ('Santiago', 'SD Compostela'),
        ('Leon', 'CyD Leonesa'),
        ('PBMadrid', 'Puerta Bonita'),
    )

#Errores por defector para los formularios
my_default_errors = {
    'required': 'Este campo es requerido',
    'invalid': 'Introduzca un valor correcto',
    'passConf': 'No existe el password',
    'passMatch': 'No coinciden los passwords',
    'regisUser': 'Usuario ya registrado',
}
        
class LoginForm(forms.Form):
        subject = forms.CharField(max_length=100)
        message = forms.CharField()
        sender = forms.EmailField()
        cc_myself = forms.BooleanField(required=False)

class RegisterForm(forms.Form):
        #------ Genero -----------#
        genero = forms.ChoiceField (            widget=forms.RadioSelect(attrs={'class':'input-xlarge'}),
                                                choices=GENERE_CHOICES, label = "Genero : ",  error_messages=my_default_errors )
        #------ Nombre -----------#
        nombre = forms.CharField(               required=True, widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Nombre'}),
                                                label = "Nombre : ", error_messages=my_default_errors)
        #------ Apellidos --------#
        apellidos = forms.CharField(            required=True, widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Apellidos'}),
                                                label = "Apellidos : ", error_messages=my_default_errors)
        #------ Tipo doc ---------#
        tipo_documento = forms.ChoiceField(     required=True, widget=forms.Select(attrs={'class':'input-xlarge'}),
                                                choices=TIPDOC_CHOICES, label = "Tipo de documento : ",
                                                error_messages=my_default_errors)
        #------ Numero doc -------#
        numero_documento = forms.CharField(     required=True, widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Numero documento'}),
                                                label = "Numero de documento : ", error_messages=my_default_errors)
        #------ Nombre user ------#
        nombre_usuario = forms.CharField(       required=True, widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Usuario'}),
                                                label = "Nombre de usuario : ", error_messages=my_default_errors)
        #------ Apellidos --------#
        password = forms.CharField(             required=True, widget=forms.PasswordInput(attrs={'class':'input-xlarge','placeholder':'Password'}),
                                                label = "Password : ", max_length=100, error_messages=my_default_errors)
        #------ Apellidos --------#
        repassword = forms.CharField(           required=True, widget=forms.PasswordInput(attrs={'class':'input-xlarge','placeholder':'rePassword'}),
                                                label = "Re-Password : ", max_length=100, error_messages=my_default_errors)
        #------ Apellidos --------#
        email = forms.EmailField(               required=True, widget=forms.TextInput(attrs={'class':'input-xlarge','placeholder':'Email'}),
                                                label = "E-mail : ", error_messages=my_default_errors)

class PublicaForm(forms.Form):
        salida = forms.ChoiceField (            widget=forms.Select(attrs={'class':'input-xlarge'}),
                                                choices=CITY_CHOICES, label = "Desde : ",  error_messages=my_default_errors )
        
        destino = forms.ChoiceField (           widget=forms.Select(attrs={'class':'input-xlarge'}),
                                                choices=CITY_CHOICES, label = "Hasta : ",  error_messages=my_default_errors )
        
        fechasal = forms.DateTimeField (        widget=forms.TextInput(attrs={'class':'input-xlarge','data-format':'yyyy-MM-dd hh:mm:ss'}), 
                                                label = "Fecha salida : ",  error_messages=my_default_errors)
        
        fecharet = forms.DateTimeField (        widget=forms.TextInput(attrs={'class':'input-xlarge','data-format':'yyyy-MM-dd hh:mm:ss'}), 
                                                label = "Fecha llegada : ", error_messages=my_default_errors)
        
        plazas = forms.IntegerField (           widget=forms.TextInput(attrs={'class':'input-xlarge'}),
                                                label = "Plazas ofertadas : ", error_messages=my_default_errors,
                                                max_value = 100, min_value = 1)        
        
        
        
        
        
        
        
        
        