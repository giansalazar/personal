from rest_framework import routers
from .api import *
router = routers.DefaultRouter()

router.register('api/personas', PersonasViewSet, 'personas')
router.register('api/empleados', EmpleadosViewSet, 'empleados')
router.register('api/puestos', PuestosViewSet, 'puestos')
router.register('api/jefaturas', JefaturasViewSet, 'jefaturas')

urlpatterns = router.urls