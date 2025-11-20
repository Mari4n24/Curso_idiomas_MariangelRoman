from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio/inicio.html')

def about(request):
    return render(request, 'about.html')