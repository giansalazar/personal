from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import *

class EmpleadosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleados
        fields = ('id', 'id_persona', 'id_puesto',)

class PersonasSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'nombre', 'apep', 'apem', 'genero', 'username', 'id_persona', 'telefono', 'email',)
        read_only_field = ('is_staff', 'is_active', 'objects')
        extra_kwargs = {'password':{'write_only':True, 'min_length':8}}

        def create(self, validated_data):
            return get_user_model().objects.create_user(**validated_data)

class PuestosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Puestos
        fields = ('id', 'nombre', 'id_jefatura',)

class JefaturasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Jefaturas
        fields = ('id', 'nombre',)
