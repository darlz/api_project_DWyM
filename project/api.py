from .models import User, Curso, Matricula
from rest_framework import viewsets, permissions
from .serializers import UserSerializer, CursoSerializer, MatriculaSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CursoSerializer


class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MatriculaSerializer
