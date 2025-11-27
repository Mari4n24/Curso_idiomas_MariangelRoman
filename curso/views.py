from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Curso, Alumno, Profesor
from .forms import CursoForm, AlumnoForm, ProfesorForm

# Cursos

@login_required
def listar_cursos(request):
    query = request.GET.get('buscar')
    if query:
        cursos = Curso.objects.filter(idioma__icontains=query)
        mensaje = 'o se encontraron cursos' if not cursos else ''
    else:
        cursos = Curso.objects.all()
        mensaje = 'No hay cursos cargados' if not cursos else ''
    return render(request, 'curso/listar_curso.html', {'cursos': cursos, 'mensaje': mensaje})

@login_required 
def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'curso/crear_curso.html', {'form': form})

class CursoDetalleView(LoginRequiredMixin,DetailView):
    model = Curso
    template_name = 'curso/detalle_curso.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class CursoEditarView(LoginRequiredMixin, UpdateView):
    model = Curso
    form_class = CursoForm
    template_name = 'curso/editar_curso.html'
    success_url = reverse_lazy('listar_cursos')

class CursoBorrarView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'curso/borrar_curso.html'
    success_url = reverse_lazy('listar_cursos')

# Alumnos

@login_required
def listar_alumnos(request):
    alumnos = Alumno.objects.all()
    mensaje = 'No hay alumnos cargados' if not alumnos else ''
    return render(request, 'curso/listar_alumnos.html', {'alumnos': alumnos, 'mensaje': mensaje})

@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'curso/crear_alumno.html', {'form': form})

# Profesores
@login_required
def listar_profesores(request):
    profesores = Profesor.objects.all()
    mensaje = 'No hay profesores cargados' if not profesores else ''
    return render(request, 'curso/listar_profesores.html', {'profesores': profesores, 'mensaje': mensaje})    

@login_required
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'curso/crear_profesor.html', {'form': form})