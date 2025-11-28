from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'alumno/listar_alumnos.html', {'alumnos': alumnos, 'mensaje': mensaje})

@login_required
def crear_alumno(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alumnos')
    else:
        form = AlumnoForm()
    return render(request, 'alumno/crear_alumno.html', {'form': form})

@login_required
def editar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)
    form = AlumnoForm(request.POST or None, request.FILES or None, instance=alumno)


    if form.is_valid():
        form.save()
        return redirect('listar_alumnos')

    return render(request, 'alumno/editar_alumno.html', {'form': form})

@login_required
def borrar_alumno(request, pk):
    alumno = get_object_or_404(Alumno, pk=pk)

    if request.method == 'POST':
        alumno.delete()
        return redirect('listar_alumnos')

    return render(request, 'alumno/borrar_alumno.html', {'alumno': alumno})



# Profesores
@login_required
def listar_profesores(request):
    profesores = Profesor.objects.all()
    mensaje = 'No hay profesores cargados' if not profesores else ''
    return render(request, 'profesor/listar_profesores.html', {'profesores': profesores, 'mensaje': mensaje})    

@login_required
def crear_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'profesor/crear_profesor.html', {'form': form})

@login_required
def editar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)
    form = ProfesorForm(request.POST or None, request.FILES or None, instance=profesor)

    if form.is_valid():
        form.save()
        return redirect('listar_profesores')

    return render(request, 'profesor/editar_profesor.html', {'form': form})

@login_required
def borrar_profesor(request, pk):
    profesor = get_object_or_404(Profesor, pk=pk)

    if request.method == 'POST':
        profesor.delete()
        return redirect('listar_profesores')

    return render(request, 'profesor/borrar_profesor.html', {'profesor': profesor})
