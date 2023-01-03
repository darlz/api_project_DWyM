from django.db import models

# Create your models here.
class User(models.Model):
    nombre = models.CharField(max_length=100)
    apellido =models.CharField(max_length=100)
    cedula = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    def __str__(self):
        return self.email


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    description= models.TextField()
    instructor = models.CharField(max_length=100)


class Matricula(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    
