from pyexpat import model
from django.db import models


# aca creamos la conexion con todas las diferentes tablas de la base de datos por medio de clases asi:
class libros (models.Model):
    ID_Libro = models.PositiveIntegerField(max_length=40, primary_key=True) # aca indicamos la llave primaria que ayuda a la conexion con las otras tablas
    Nombre_Libro = models.CharField(max_length=80) #charfield indica el tipo de dato que la tabla va a recibir y la extension del texto
    Autor = models.CharField(max_length=80) #
    Estado = models.CharField(max_length=40)
    
    def __str__(self):
        txt = 'Título: ' + self.Nombre_Libro 
        return txt



class prestamos (models.Model):
    ID_Libro = models.PositiveIntegerField (max_length=40, primary_key=True)
    ID_User = models.PositiveIntegerField (max_length=20)
    Estado = models.CharField (max_length=20)
    Fecha_inicio = models.DateField ()
    Fecha_fin = models.DateField ()

    def __str__(self):
        txt = 'Id: ' + str(self.ID_Libro) + '-' + 'Estado: ' + self.Estado 
        return txt

class usuarios (models.Model):
    ID_User = models.PositiveIntegerField (max_length=20, primary_key=True)
    Nombre_Usuario = models.CharField (max_length=40)
    Direccion_Usuario = models.CharField (max_length=60)

    def __str__(self):
        txt = 'Id: ' + str(self.ID_User) + '-' + self.Nombre_Usuario 
        return txt





