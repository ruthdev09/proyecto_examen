from django.contrib import admin
from .models import Curso, Estudiante

# Esto hace que aparezcan en la pantalla que tienes abierta
admin.site.register(Curso)
admin.site.register(Estudiante)