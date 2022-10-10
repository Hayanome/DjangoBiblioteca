from django.urls import path
from .views import *
from . import views

#se crea una lista en la cual se establece una ruta con la clase
# creada en views.py 
urlpatterns = [
    path ('index', views.index, name='index'),
    path ('libros', views.resultados, name='libros' ),
    path ('consulta', views.consulta, name='consulta')
]