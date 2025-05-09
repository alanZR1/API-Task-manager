from django.db import models

# Create your models here.
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    completada = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre