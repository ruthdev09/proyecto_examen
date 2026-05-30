from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Estudiante, Curso
from .forms import EstudianteForm, CursoForm


# ==========================================
# CRUD DE ESTUDIANTES
# ==========================================

def listar_estudiantes(request):
    estudiantes = Estudiante.objects.select_related('curso').all()
    return render(request, 'estudiantes/listar.html', {'estudiantes': estudiantes})


def crear_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Estudiante registrado correctamente.')
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'estudiantes/form.html', {'form': form, 'titulo': 'Registrar Estudiante'})


def editar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    if request.method == 'POST':
        form = EstudianteForm(request.POST, request.FILES, instance=estudiante)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Estudiante actualizado correctamente.')
            return redirect('listar_estudiantes')
    else:
        form = EstudianteForm(instance=estudiante)
    return render(request, 'estudiantes/form.html', {
        'form': form,
        'titulo': f'Editar Estudiante: {estudiante.nombre} {estudiante.apellido}',
        'editando': True,
    })


def eliminar_estudiante(request, pk):
    estudiante = get_object_or_404(Estudiante, pk=pk)
    nombre = f"{estudiante.nombre} {estudiante.apellido}"
    estudiante.delete()
    messages.success(request, f'🗑️ Estudiante "{nombre}" eliminado.')
    return redirect('listar_estudiantes')


# ==========================================
# CRUD DE CURSOS
# ==========================================

def listar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/listar_cursos.html', {'cursos': cursos})


def crear_curso(request):
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Curso creado correctamente.')
            return redirect('listar_cursos')
    else:
        form = CursoForm()
    return render(request, 'cursos/form_curso.html', {'form': form, 'titulo': 'Crear Nuevo Curso'})


def editar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        form = CursoForm(request.POST, request.FILES, instance=curso)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Curso actualizado correctamente.')
            return redirect('listar_cursos')
    else:
        form = CursoForm(instance=curso)
    return render(request, 'cursos/form_curso.html', {
        'form': form,
        'titulo': f'Editar Curso: {curso.nombre}',
        'editando': True,
    })


def eliminar_curso(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    nombre = curso.nombre
    curso.delete()
    messages.success(request, f'🗑️ Curso "{nombre}" eliminado.')
    return redirect('listar_cursos')
