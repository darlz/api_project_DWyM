from rest_framework import routers
from .api import UserViewSet, CursoViewSet, MatriculaViewSet

router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')
router.register('api/cursos', CursoViewSet, 'cursos')
router.register('api/matriculas', MatriculaViewSet, 'matriculas')

urlpatterns = router.urls
