from django.db import models

class Curso(models.Model):
    nivel = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True)
