from django.shortcuts import render, redirect
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_curso.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        idioma = request.POST.get('idioma')
        nivel = request.POST.get('nivel')
        imagen = request.FILES.get('imagen')

        Curso.objects.create(
            idioma=idioma,
            nivel=nivel,
            imagen=imagen
        )

        return redirect('listar_cursos')

    return render(request, 'curso/crear_curso.html')