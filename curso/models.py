from django.db import models

class Curso(models.Model):
    nivel = models.CharField(max_length=20)
    idioma = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='cursos', null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.idioma} - {self.nivel}'

class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    imagen = models.ImageField(upload_to='alumnos/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'

class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=30)
    cursos = models.ManyToManyField(Curso, blank=True)
    imagen = models.ImageField(upload_to='profesores/', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre}'