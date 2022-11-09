from .models import *
from rest_framework import viewsets, permissions
from .serializers import *

class PersonasViewSet(viewsets.ModelViewSet):
    
    queryset = Personas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PersonasSerializer

class EmpleadosViewSet(viewsets.ModelViewSet):
    
    queryset = Empleados.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EmpleadosSerializer

class PuestosViewSet(viewsets.ModelViewSet):
    
    queryset = Puestos.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PuestosSerializer

class JefaturasViewSet(viewsets.ModelViewSet):
    
    queryset = Jefaturas.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = JefaturasSerializer