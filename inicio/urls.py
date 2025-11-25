from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('inicio/about/', about, name='about'),
]
