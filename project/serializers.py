from rest_framework import serializers
from .models import User, Curso, Matricula

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'nombre', 'apellido', 'cedula', 'telefono', 'email')
        read_only_fields = ('id',)

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'nombre', 'description', 'instructor')
        read_only_fields = ('id',)

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = ('id', 'id_user', 'id_curso')
        read_only_fields = ('id',)