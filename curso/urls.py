from django.urls import path
from .views import *

urlpatterns = [
    path('listar/', listar_cursos, name='listar_cursos'),
    path('crear/', crear_curso, name='crear_curso'),
    path('<int:pk>/', CursoDetalleView.as_view(), name='detalle_curso'),
    path('<int:pk>/editar/', CursoEditarView.as_view(), name='editar_curso'),
    path('<int:pk>/borrar/', CursoBorrarView.as_view(), name='borrar_curso'),
    path('alumnos/listar/', listar_alumnos, name='listar_alumnos'),
    path('alumnos/crear/', crear_alumno, name='crear_alumno'),
    path('profesores/listar/', listar_profesores, name='listar_profesores'),
    path('profesores/crear/', crear_profesor, name='crear_profesor'),
]
