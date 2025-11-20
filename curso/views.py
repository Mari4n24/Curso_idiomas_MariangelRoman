from django.shortcuts import render, redirect
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_curso.html', {'cursos': cursos})

def crear_curso(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        idioma = request.POST['idioma']
        nivel = request.POST['nivel']
        profesor = request.POST['profesor']
        imagen = request.FILES.get('imagen')
        
        Curso.objects.create(
            nombre=nombre,
            idioma=idioma,
            nivel=nivel,
            profesor=profesor,
            imagen=imagen
        )
        
        return redirect('listar_cursos')
    
    return render(request, 'curso/crear_curso.html')