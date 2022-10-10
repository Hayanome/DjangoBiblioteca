#este programa se crea de cero lo que hace es llamar el html creado y añadido a la carpeta web

from django.shortcuts import render


def index(request):
    return render(request, "web/index.html")

#def resultado(request):
#    if request.method == 'get':
#        pass 