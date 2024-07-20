from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()
    codigo = models.CharField(max_length=10)
    imagen = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.nombre} - {self.comision}'


class Estudiante(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Profesor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    profesion = models.CharField(max_length=50)
    cursos = models.ManyToManyField(Curso)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    estudiante = models.ManyToManyField(Estudiante)

    def __str__(self):
        return f'{self.nombre} - {self.fecha_entrega}'


class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"  