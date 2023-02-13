from django.contrib import admin

# Register your models here.
from .models import Tipodispositivo
from .models import Dispositivo
from .models import Asignacion
from .models import Usuario
admin.site.register(Tipodispositivo)
admin.site.register(Dispositivo)
admin.site.register(Asignacion)
admin.site.register(Usuario)