from django.urls import path
from . import views

urlpatterns = [
    # URLs de Estudiantes
    path('', views.listar_estudiantes, name='listar_estudiantes'),
    path('nuevo/', views.crear_estudiante, name='crear_estudiante'),
    path('editar/<str:pk>/', views.editar_estudiante, name='editar_estudiante'),
    path('eliminar/<str:pk>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # URLs de Cursos
    path('cursos/', views.listar_cursos, name='listar_cursos'),
    path('cursos/nuevo/', views.crear_curso, name='crear_curso'),
    path('cursos/editar/<int:pk>/', views.editar_curso, name='editar_curso'),
    path('cursos/eliminar/<int:pk>/', views.eliminar_curso, name='eliminar_curso'),
] 