from django import forms
from .models import Curso, Alumno, Profesor

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['idioma', 'nivel', 'imagen']

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre', 'apellido', 'email']

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = ['nombre', 'especialidad', 'cursos']
        widgets = {
            'cursos': forms.CheckboxSelectMultiple(),
        }