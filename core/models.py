from django.db import models

class Curso(models.Model):
    # Campos: 1.Nombre, 2.Docente, 3.Créditos, 4.Foto
    nombre = models.CharField(max_length=100)
    docente = models.CharField(max_length=100)
    creditos = models.IntegerField()
    foto_curso = models.ImageField(upload_to='cursos/', null=True, blank=True) # IMAGEN PARA CURSO

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    # Campos: 1.ID, 2.Nombre, 3.Email, 4.Foto + Relación
    id_estudiante = models.CharField(max_length=20, primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    foto = models.ImageField(upload_to='estudiantes/', null=True, blank=True) # IMAGEN PARA ESTUDIANTE
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}" 