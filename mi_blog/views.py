from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.shortcuts import render, redirect
from .models import Familiares, Amigos, Viajes
from .forms import FamiliaresForm, AmigosForm, ViajesForm,BusquedaForm

def lista_familiares(request):
    familiares = Familiares.objects.all()
    return render(request, 'mi_blog/lista_familiares.html', {'familiares': familiares})


def lista_amigos(request):
    amigos = Amigos.objects.all()
    return render(request, 'mi_blog/lista_amigos.html', {'amigos': amigos})

def lista_viajes(request):
    viajes = Viajes.objects.all()
    return render(request, 'mi_blog/lista_viajes.html', {'viajes': viajes})

def crear_familiar(request):
    if request.method == 'POST':
        form = FamiliaresForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:crear_familiar')
    else:
        form = FamiliaresForm()
    return render(request, 'mi_blog/crear_familiar.html', {'form': form})

def crear_amigo(request):
    if request.method == 'POST':
        form = AmigosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:lista_amigos')
    else:
        form = AmigosForm()
    return render(request, 'mi_blog/crear_amigo.html', {'form': form})

def crear_viaje(request):
    if request.method == 'POST':
        form = ViajesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mi_blog:lista_viajes')
    else:
        form = ViajesForm()
    return render(request, 'mi_blog/crear_viaje.html', {'form': form})

def buscar(request):
    if request.method == 'POST':
        # Realiza una búsqueda en la base de datos
        term = request.POST.get('termino_busqueda')
        resultados_familiares = Familiares.objects.filter(nombre__icontains=term)
        resultados_amigos = Amigos.objects.filter(nombre__icontains=term)
        resultados_viajes = Viajes.objects.filter(destino__icontains=term)
        return render(request, 'mi_blog/resultados_busqueda.html', {
            'resultados_familiares': resultados_familiares,
            'resultados_amigos': resultados_amigos,
            'resultados_viajes': resultados_viajes
        })
    else:
        form = BusquedaForm()
        return render(request,'mi_blog/buscar.html',{'form':form})
    
def eliminar_familiar(request, id):
    # obtienes el curso de la base de datos
    familiares = Familiares.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        familiares.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('mi_blog:lista_familiares')
        return redirect(url_exitosa)
    
def eliminar_amigo(request, id):
    # obtienes el curso de la base de datos
    amigos = Amigos.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        amigos.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('mi_blog:lista_amigos')
        return redirect(url_exitosa)
    
def eliminar_viaje(request, id):
    # obtienes el curso de la base de datos
    viajes = Viajes.objects.get(id=id)
    if request.method == "POST":
        # borra el curso de la base de datos
        viajes.delete()
        # redireccionamos a la URL exitosa
        url_exitosa = reverse('mi_blog:lista_viajes')
        return redirect(url_exitosa)


def editar_familiar(request, id):
    familiares = Familiares.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        form = FamiliaresForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            # modificamos el objeto en memoria RAM
            familiares.apellido = data['apellido']
            familiares.nombre = data['nombre']
            familiares.fecha_nacimiento = data['fecha_nacimiento']
            familiares.parentesco = data['parentesco']
            # Los cambios se guardan en la Base de datos
            familiares.save()

            url_exitosa = reverse('mi_blog:lista_familiares')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'apellido': familiares.apellido,
            'nombre': familiares.nombre,
            'fecha_nacimiento': familiares.fecha_nacimiento,
            'parentesco': familiares.parentesco,
        }
        form = FamiliaresForm(initial=inicial)
    return render(
        request=request,
        template_name='mi_blog/crear_familiar.html',
        context={'form': form},
    )

def editar_viaje(request, id):
    viajes = Viajes.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        form = ViajesForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            # modificamos el objeto en memoria RAM
            viajes.destino = data['destino']
            viajes.fecha_viaje = data['fecha_viaje']
            viajes.duracion = data['duracion']
            viajes.viajeros = data['viajeros']

            # Los cambios se guardan en la Base de datos
            viajes.save()

            url_exitosa = reverse('mi_blog:lista_viajes')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'destino': viajes.destino,
            'fecha_viaje': viajes.fecha_viaje,
            'duracion': viajes.duracion,
            'viajeros': viajes.viajeros,
        }
        form = ViajesForm(initial=inicial)
    return render(
        request=request,
        template_name='mi_blog/crear_viaje.html',
        context={'form': form},
    )


def editar_amigo(request, id):
    amigos = Amigos.objects.get(id=id)
    if request.method == "POST":
        # Actualizacion de datos
        form = AmigosForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            # modificamos el objeto en memoria RAM
            amigos.apellido = data['apellido']
            amigos.nombre = data['nombre']
            amigos.fecha_nacimiento = data['fecha_nacimiento']
            amigos.nivel_amistad = data['nivel_amistad']
            # Los cambios se guardan en la Base de datos
            amigos.save()

            url_exitosa = reverse('mi_blog:lista_amigos')
            return redirect(url_exitosa)
    else:  # GET
        # Descargar formulario con data actual
        inicial = {
            'apellido': amigos.apellido,
            'nombre': amigos.nombre,
            'fecha_nacimiento': amigos.fecha_nacimiento,
            'nivel_amistad' : amigos.nivel_amistad
        }
        form = AmigosForm(initial=inicial)
    return render(
        request=request,
        template_name='mi_blog/crear_amigo.html',
        context={'form': form},
    )