from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    nivel = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True)
