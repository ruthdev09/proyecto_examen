from django import forms
from .models import Estudiante, Curso

# Atributos CSS comunes para los inputs
INPUT_CLASS  = 'form-control'
SELECT_CLASS = 'form-control'

WIDGET_ATTRS = {'class': INPUT_CLASS}


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
        widgets = {
            'nombre':    forms.TextInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Ej: Programación Web'}),
            'docente':   forms.TextInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Ej: Dr. Juan Pérez'}),
            'creditos':  forms.NumberInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Ej: 4', 'min': 1, 'max': 10}),
            'foto_curso': forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
        }
        labels = {
            'nombre':    'Nombre del Curso',
            'docente':   'Docente Responsable',
            'creditos':  'Créditos',
            'foto_curso': 'Imagen / Banner del Curso',
        }


class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = '__all__'
        widgets = {
            'id_estudiante': forms.TextInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Ej: EST-001'}),
            'nombre':        forms.TextInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Nombre(s)'}),
            'apellido':      forms.TextInput(attrs={**WIDGET_ATTRS, 'placeholder': 'Apellido(s)'}),
            'email':         forms.EmailInput(attrs={**WIDGET_ATTRS, 'placeholder': 'correo@ejemplo.com'}),
            'foto':          forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
            'curso':         forms.Select(attrs={'class': SELECT_CLASS}),
        }
        labels = {
            'id_estudiante': 'ID del Estudiante',
            'nombre':        'Nombre(s)',
            'apellido':      'Apellido(s)',
            'email':         'Correo Electrónico',
            'foto':          'Foto del Estudiante',
            'curso':         'Curso Asignado',
        }
