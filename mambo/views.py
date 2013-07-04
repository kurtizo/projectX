#encoding:utf-8
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from account.models import UserProfile
from form.codeForm import LoginForm, RegisterForm


#Página principal
def index_view(request):
    return render_to_response('principal.html', RequestContext(request))

# Vista correspondiente al logout
def logout_view(request):
    logout(request)
    return render_to_response('principal.html', RequestContext(request))

# Vista correspondiente al login
def login_view(request):
        if request.method == 'POST':
            # Obtenemos del formulario de login los datos para la autentificación
                formLogin = LoginForm(request.POST)
                username = request.POST.get('username')
                password = request.POST.get('password')
            # Autenticamos al usuario con las lib de django
                user = authenticate(username=username, password=password)
                if user is not None:
                        if user.is_active:
                            login(request, user)
                            profile = UserProfile(get_user_model())
                            request.profile = profile
                            print dir(profile)
                            print "Apellidos"
                            print profile.object.get(username=user)
                            print profile.get_full_name()
                            # Recuperamos el perfil y lo insertamos como parte de la request
                            return render_to_response('principal.html', RequestContext(request))
                        else:
                                print "Usuario nefasto"
                        
        else:
            formLogin = LoginForm()    
        return render_to_response('login_activate.html', {'formLogin': formLogin,} ,RequestContext(request))

#########################################################################################################
#    Hay que realizar modificaciones sobre en formulario de creacion de usuarios                        #
#                                                                                                       #
#########################################################################################################
#Vista del registro
def register_view(request):

        if request.method == 'POST':
                formRegister    = RegisterForm(request.POST)
                if formRegister.is_valid():
                        genero          = formRegister.cleaned_data['genero']
                        nombre          = formRegister.cleaned_data['nombre']
                        apellidos       = formRegister.cleaned_data['apellidos']
                        tipoDoc         = formRegister.cleaned_data['tipo_documento']
                        numeroDoc       = formRegister.cleaned_data['numero_documento']
                        user            = formRegister.cleaned_data['nombre_usuario']
                        password        = formRegister.cleaned_data['password']
                        email           = formRegister.cleaned_data['email']
                        nacimiento      = formRegister.cleaned_data['nacimiento']
                        #Se crea el usuario
                        User.objects.create_user(user, password, genero, nombre, apellidos, tipoDoc, numeroDoc, nacimiento, email)
                        #Se crea el perfil del usuario
                        # UserProfile.objects.create(genero=genero, nombre=nombre, apellidos=apellidos,
                        #                            tipoDoc=tipoDoc, numeroDoc=numeroDoc, user=user,
                        #                            email=email )
                        
                        return render_to_response('principal.html', RequestContext(request))
                        
        else:
                formRegister = RegisterForm()

        return render_to_response('register_form.html',  {'formRegister': formRegister,} ,RequestContext(request))
 
#Vista del menú de búsqueda
def search_view(request):
        return render_to_response('search_form.html',  RequestContext(request))

#Vista del menú de contacto
def contact_view(request):
        return render_to_response('contacto.html',  RequestContext(request))

#Vista del menú de perfil
def perfil_view(request):
        profile = UserProfile(get_user_model())
        request.profile = profile
        print dir(profile._meta.get_field('apellidos'))
        print "Apellidos"
        return render_to_response('perfil.html',  RequestContext(request))


