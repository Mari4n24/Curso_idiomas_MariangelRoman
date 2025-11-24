from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView, DeleteView
from .models import Curso

@login_required
def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'curso/listar_curso.html', {'cursos': cursos})

@login_required 
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

class CursoDetalleView(LoginRequiredMixin,DetailView):
    model = Curso
    template_name = 'curso/detalle_curso.html'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class CursoEditarView(LoginRequiredMixin, UpdateView):
    model = Curso
    fields = ['idioma', 'nivel', 'imagen']
    template_name = 'curso/editar_curso.html'
    success_url = reverse_lazy('listar_cursos')

class CursoBorrarView(LoginRequiredMixin, DeleteView):
    model = Curso
    template_name = 'curso/borrar_curso.html'
    success_url = reverse_lazy('listar_cursos')