from django.contrib import admin
from django.urls import path
from django.urls import include

#se importa abajo la union entre el archivo creado vista con esta pagina
from myproject.vista import index

urlpatterns = [
    path('admin/', admin.site.urls),
    #coneccion con el archivo urls dentro de la carpeta api
    path('', include('api.urls'))
]
