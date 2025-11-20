from django.shortcuts import render
from .models import Curso

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_cursos.html', {'cursos': cursos})