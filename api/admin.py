from django.contrib import admin

from api.models import * #importante hacer la importacion aunque visual lo hace solo

admin.site.register(libros) #asi hacemos con cada clase para poder darle uso acá
admin.site.register(prestamos)
admin.site.register(usuarios)
# Register your models here.
