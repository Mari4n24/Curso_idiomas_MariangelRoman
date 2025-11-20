from django.urls import path
from .views import listar_cursos, crear_curso, CursoDetalleView, CursoEditarView, CursoBorrarView

urlpatterns = [
    path('listar/', listar_cursos, name='listar_cursos'),
    path('crear/', crear_curso, name='crear_curso'),
    path('<int:pk>/', CursoDetalleView.as_view(), name='detalle_curso'),
    path('<int:pk>/editar/', CursoEditarView.as_view(), name='editar_curso'),
    path('<int:pk>/borrar/', CursoBorrarView.as_view(), name='borrar_curso'),
]
