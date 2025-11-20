from django.urls import path
from .views import listar_cursos, crear_curso

urlpatterns = [
    path('listar/', listar_cursos, name='listar_cursos'),
    path('crear/', crear_curso, name='crear_curso'),
]
