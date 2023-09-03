###Librerias Importadas
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

###Funcion Home / HTML Base

def home(request):
    return render(request, 'mainapp/base.html')

###Funciones WEB / Modulos / CRUD para cada Funcion-Forms

############Modulo de Guitarras
@login_required
def guitarras(request):
    contexto = {'guitarras': Guitarra.objects.all(), 'titulo':'Listado de Guitarras' }
    return render(request, 'mainapp/guitarras.html', contexto)

###Actualizacion Guitarras
@login_required
def updateGuitarras(request, id_guitarra):
    guitarras = Guitarra.objects.get(id=id_guitarra)
    if request.method == "POST":
        miForm = GuitarrasForm(request.POST)
        if miForm.is_valid():
            guitarras.marca = miForm.cleaned_data.get('marca')
            guitarras.modelo = miForm.cleaned_data.get('modelo')
            guitarras.origen = miForm.cleaned_data.get('origen')
            guitarras.precio = miForm.cleaned_data.get('precio')
            guitarras.save()
            return redirect(reverse_lazy('guitarras')) 
 
    else:
        miForm = GuitarrasForm(initial={
            'marca': guitarras.marca,
            'modelo': guitarras.modelo,
            'origen': guitarras.origen,
            'precio': guitarras.precio,
        })
    return render(request, 'mainapp/guitarrasForm.html', {'form': miForm})

###Eliminar Guitarras
@login_required
def deleteGuitarras(request, id_guitarra):
    guitarras = Guitarra.objects.get(id=id_guitarra)
    guitarras.delete()
    return redirect(reverse_lazy('guitarras'))

###Crear Guitarras
@login_required
def createGuitarras(request):    
    if request.method == "POST":
        miForm = GuitarrasForm(request.POST)
        if miForm.is_valid():
            r_marca = miForm.cleaned_data.get('marca')
            r_modelo = miForm.cleaned_data.get('modelo')
            r_origen = miForm.cleaned_data.get('origen')
            r_precio = miForm.cleaned_data.get('precio')
            guitarras = Guitarra(marca=r_marca, 
                            modelo=r_modelo,
                            origen=r_origen,
                            precio=r_precio,
                            )
            guitarras.save()
            return redirect(reverse_lazy('guitarras'))
    else:
        miForm = GuitarrasForm()

    return render(request, 'mainapp/guitarrasForm.html', {'form':miForm})

###Buscar Guitarras
@login_required
def buscarGuitarras(request):
    return render(request, 'mainapp/buscarGuitarras.html')

@login_required
def buscar1(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        guitarras = Guitarra.objects.filter(marca__icontains=patron)
        contexto = {'guitarras': guitarras} 
        return render(request, 'mainapp/guitarras.html', contexto)
    return HttpResponse("No ingreso un dato valido.")

############Modulo de Bajos
@login_required
def bajos(request):
    contexto = {'bajos': Bajo.objects.all(), 'titulo':'Listado de Bajos' }
    return render(request, 'mainapp/bajos.html', contexto)

###Actualizacion Bajos
@login_required
def updateBajos(request, id_bajo):
    bajos = Bajo.objects.get(id=id_bajo)
    if request.method == "POST":
        miForm = BajosForm(request.POST)
        if miForm.is_valid():
            bajos.marca = miForm.cleaned_data.get('marca')
            bajos.modelo = miForm.cleaned_data.get('modelo')
            bajos.origen = miForm.cleaned_data.get('origen')
            bajos.precio = miForm.cleaned_data.get('precio')
            bajos.save()
            return redirect(reverse_lazy('bajos')) 
 
    else:
        miForm = BajosForm(initial={
            'marca': bajos.marca,
            'modelo': bajos.modelo,
            'origen': bajos.origen,
            'precio': bajos.precio,
        })
    return render(request, 'mainapp/bajosForm.html', {'form': miForm})

###Eliminar Bajos
@login_required
def deleteBajos(request, id_bajo):
    bajos = Bajo.objects.get(id=id_bajo)
    bajos.delete()
    return redirect(reverse_lazy('bajos'))

###Crear Bajos
@login_required
def createBajos(request):    
    if request.method == "POST":
        miForm = BajosForm(request.POST)
        if miForm.is_valid():
            r_marca = miForm.cleaned_data.get('marca')
            r_modelo = miForm.cleaned_data.get('modelo')
            r_origen = miForm.cleaned_data.get('origen')
            r_precio = miForm.cleaned_data.get('precio')
            bajos = Bajo(marca=r_marca, 
                            modelo=r_modelo,
                            origen=r_origen,
                            precio=r_precio,
                            )
            bajos.save()
            return redirect(reverse_lazy('bajos'))
    else:
        miForm = BajosForm()

    return render(request, 'mainapp/bajosForm.html', {'form':miForm})

###Buscar Bajos
@login_required
def buscarBajos(request):
    return render(request, 'mainapp/buscarBajos.html')

@login_required
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        bajos = Bajo.objects.filter(marca__icontains=patron)
        contexto = {'bajos': bajos} 
        return render(request, 'mainapp/bajos.html', contexto)
    return HttpResponse("No ingreso un dato valido.")



############Modulo de Percusion
@login_required
def percusion(request):
    contexto = {'percusion': Percusion.objects.all(), 'titulo':'Listado de Percusión' }
    return render(request, 'mainapp/percusion.html', contexto)

###Actualizacion Percusion
@login_required
def updatePercusion(request, id_percusion):
    percusion = Percusion.objects.get(id=id_percusion)
    if request.method == "POST":
        miForm = PercusionForm(request.POST)
        if miForm.is_valid():
            percusion.marca = miForm.cleaned_data.get('marca')
            percusion.modelo = miForm.cleaned_data.get('modelo')
            percusion.origen = miForm.cleaned_data.get('origen')
            percusion.precio = miForm.cleaned_data.get('precio')
            percusion.save()
            return redirect(reverse_lazy('percusion')) 
 
    else:
        miForm = PercusionForm(initial={
            'marca': percusion.marca,
            'modelo': percusion.modelo,
            'origen': percusion.origen,
            'precio': percusion.precio,
        })
    return render(request, 'mainapp/percusionForm.html', {'form': miForm})

###Eliminar Percusion
@login_required
def deletePercusion(request, id_percusion):
    percusion = Percusion.objects.get(id=id_percusion)
    percusion.delete()
    return redirect(reverse_lazy('percusion'))

###Crear Percusion
@login_required
def createPercusion(request):    
    if request.method == "POST":
        miForm = PercusionForm(request.POST)
        if miForm.is_valid():
            r_marca = miForm.cleaned_data.get('marca')
            r_modelo = miForm.cleaned_data.get('modelo')
            r_origen = miForm.cleaned_data.get('origen')
            r_precio = miForm.cleaned_data.get('precio')
            percusion = Percusion(marca=r_marca, 
                            modelo=r_modelo,
                            origen=r_origen,
                            precio=r_precio,
                            )
            percusion.save()
            return redirect(reverse_lazy('percusion'))
    else:
        miForm = PercusionForm()

    return render(request, 'mainapp/percusionForm.html', {'form':miForm})

###Buscar Percusion
@login_required
def buscarPercusion(request):
    return render(request, 'mainapp/buscarPercusion.html')
@login_required
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        percusion = Percusion.objects.filter(marca__icontains=patron)
        contexto = {'percusion': percusion} 
        return render(request, 'mainapp/percusion.html', contexto)
    return HttpResponse("No ingreso un dato valido.")

############Modulo Sucursales
@login_required
def sucursales(request):
    contexto = {'sucursales': Sucursal.objects.all(), 'titulo':'Listado de nuestras sucursales' }
    return render(request, 'mainapp/sucursales.html', contexto)

###Actualizacion Sucursal
@login_required
def updateSucursal(request, id_sucursal):
    sucursales = Sucursal.objects.get(id=id_sucursal)
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            sucursales.nombre = miForm.cleaned_data.get('nombre')
            sucursales.direccion = miForm.cleaned_data.get('direccion')
            sucursales.email = miForm.cleaned_data.get('email')
            sucursales.telefono = miForm.cleaned_data.get('telefono')
            sucursales.save()
            return redirect(reverse_lazy('sucursales')) 
 
    else:
        miForm = SucursalForm(initial={
            'nombre': sucursales.nombre,
            'direccion': sucursales.direccion,
            'email': sucursales.email,
            'telefono': sucursales.telefono,
        })
    return render(request, 'mainapp/sucursalesForm.html', {'form': miForm})

###Eliminar Sucursal
@login_required
def deleteSucursal(request, id_sucursal):
    sucursales = Sucursal.objects.get(id=id_sucursal)
    sucursales.delete()
    return redirect(reverse_lazy('sucursales'))

###Crear Sucursal
@login_required
def createSucursal(request):    
    if request.method == "POST":
        miForm = SucursalForm(request.POST)
        if miForm.is_valid():
            r_nombre = miForm.cleaned_data.get('nombre')
            r_direccion = miForm.cleaned_data.get('direccion')
            r_email = miForm.cleaned_data.get('email')
            r_telefono = miForm.cleaned_data.get('telefono')
            sucursales = Sucursal(nombre=r_nombre, 
                            direccion=r_direccion,
                            email=r_email,
                            telefono=r_telefono,
                            )
            sucursales.save()
            return redirect(reverse_lazy('sucursales'))
    else:
        miForm = SucursalForm()

    return render(request, 'mainapp/sucursalesForm.html', {'form':miForm})

###Modulo de About Me
@login_required
def aboutMe(request):
    return render(request, 'mainapp/aboutMe.html')

###Forms

@login_required
def guitarrasform(request):
    if request.method == 'POST':
        guitarra = Guitarra(marca=request.POST['marca'],
                            modelo=request.POST['modelo'],
                            origen=request.POST['origen'],
                            precio=request.POST['modelo'])
        guitarra.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/guitarrasForm.html')

@login_required
def guitarrasform2(request):
    if request.method == 'POST':
        miform = guitarrasform(request.POST)
        if miForm.is_valid():
            guitarras_marca = miForm.cleaned_data.get('marca')
            guitarras_modelo = miForm.cleaned_data.get('modelo')
            guitarras_origen = miForm.cleaned_data.get('origen')
            guitarras_precio = miForm.cleaned_data.get('precio')
            guitarras.save()
            return render(request, "mainapp/base.html")

    else:
        miForm = guitarrasform()
    
    return render(request, "aplicacion/cursoForm2.html", {"form": miForm })

@login_required
def bajosform(request):
    if request.method == 'POST':
        bajos = bajos(marca=request.POST['marca'],
                      modelo=request.POST['modelo'],
                      origen=request.POST['origen'],
                      precio=request.POST['modelo'])
        bajos.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/bajosForm.html')

@login_required
def percusionform(request):
    if request.method == 'POST':
        percusion = Percusion(marca=request.POST['marca'],
                            modelo=request.POST['modelo'],
                            origen=request.POST['origen'],
                            precio=request.POST['modelo'])
        percusion.save()
        return HttpResponse('Se agrego el producto al listado de forma exitosa.')
    return render(request, 'mainapp/percusionForm.html')

@login_required
def buscarSucursal(request):
    return render(request, 'mainapp/buscarSucursal.html')

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        sucursales = Sucursal.objects.filter(nombre__icontains=patron)
        contexto = {'sucursales': sucursales} 
        return render(request, 'mainapp/sucursales.html', contexto)
    return HttpResponse("No ingreso un dato valido.")

### Funciones Login / Logout / Registrar Usuarios / Edicion Perfil / Avatar 

###Login
def login_request(request):
    if request.method == 'POST':
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = '/media/avatares/default.png'
                finally:
                    request.session['avatar'] = avatar

                return render(request, 'mainapp/base.html', {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, 'mainapp/login.html', {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, 'mainapp/login.html', {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, 'mainapp/login.html', {"form":miForm})   

###Registrar Usuarios
def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, 'mainapp/base.html')
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, 'mainapp/registro.html', {"form":miForm})  

###Editar Perfil
@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request,'mainapp/base.html')
        else:
            return render(request,'mainapp/editarPerfil.html', {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'mainapp/editarPerfil.html', {'form': form, 'usuario': usuario.username})

###Agregar Avatar
@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            u = User.objects.get(username=request.user)

            #Elimina el avatar viejo.
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            #Almacena el nuevo avatar.
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # Hace que la url de la imagen viaje con el request.
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen
            return render(request,'mainapp/base.html')
    else:
        form = AvatarFormulario()
    return render(request, 'mainapp/agregarAvatar.html', {'form': form })
