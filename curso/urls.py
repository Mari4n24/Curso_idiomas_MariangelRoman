from django.urls import path
from .views import listar_cursos

urlpatterns = [
    path('listar/', listar_cursos, name='listar_cursos'),
]
