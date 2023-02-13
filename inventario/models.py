from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Tipodispositivo(models.Model):
      nombre=models.CharField(max_length=255)

      def __str__(self):
            return self.nombre
    
  




class Dispositivo(models.Model):
    
    nombre=models.CharField(max_length=100)
    ordendecompra=models.CharField(max_length=10)
    descripcion=models.TextField(blank=True)
    fechavencimientogarantia=models.DateTimeField(null=True)
    precio=models.DecimalField(decimal_places=2,max_digits=10,null=True)
    dispositivo=models.ForeignKey(Tipodispositivo,on_delete=models.CASCADE)
    
 


class Usuario(models.Model):
    
    nombre=models.CharField(max_length=100)
    cedula=models.TextField(blank=True)
    fecharegistro=models.DateTimeField(null=True)
    

    
    
                    


class Asignacion(models.Model):
    
    
    descripcion=models.TextField(blank=True)
    estado=models.BooleanField(null=False,default=True)
    fecha=models.DateTimeField(auto_now_add=True)
    dispositivo =models.ForeignKey(Dispositivo,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Usuario,on_delete=models.CASCADE)


