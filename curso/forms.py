from django import forms
from .models import Curso, Alumno, Profesor

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['idioma', 'nivel', 'imagen', 'descripcion']
        widgets = {
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Escribe la descripción del curso…'
            })
        }

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