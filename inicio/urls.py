from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about, name='about'),
]
