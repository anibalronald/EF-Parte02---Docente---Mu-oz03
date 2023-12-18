from django.db import models

class Docente(models.Model):
    codigo=models.PositiveSmallIntegerField()
    nombre=models.CharField(max_length=1000)
    apellido_paterno=models.CharField(max_length=1000)
    apellido_materno=models.CharField(max_length=1000)
    dni=models.PositiveSmallIntegerField()
    fecha_nac=models.DateField()
    fecha_reg=models.DateTimeField(auto_now_add=True)