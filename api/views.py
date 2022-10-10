from multiprocessing import context
from django.shortcuts import render
from django.views import View
from django.db.models import Q
from api.models import libros

def index(request):
    return render(request, 'web/Index.html')
    # Creamos la clase que va a mostrar los datos solicitados de la base de datos

def resultados(request):
    resultados = libros.objects.filter(Estado='Disponible').order_by('Nombre_Libro')
    return render (request, 'web/Index.html', {'resultados': resultados})
    #esta clase permite mostrar los libros de la base de datos solo si está agregado en el archivo urls de la carpeta api

def consulta (request):
    if request.method == "get":
        consulta = request.get.GET['consulta']
        busqueda = libros.objects.filter(Nombre_Libro__icontains=consulta)
    else:
        busqueda = libros.objects.all()
    context = {
        'consulta': busqueda
    }
    return render(request, 'web/resultado.html', context)
    
    # if request.method == "POST":
    #     busqueda = request.POST["consulta"]
    #     resultados = libros.objects.filter(Q(Nombre_Libro__icontains=consulta)).distinct
    #     print(resultados)
    #     #respuesta = libros.objects.filter(Nombre_Libro = busqueda)
    #     #return render(request, 'web/resultado.html',{'busqueda' :busqueda, 'resultado' :respuesta})
    #     return render(request, 'web/resultado.html',{'consulta' :list(resultados)})
    # else:
    #     return render(request,'web/resultado.html')
    