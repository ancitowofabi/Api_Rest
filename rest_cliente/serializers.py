from rest_framework import serializers
from manguera.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Cliente
        fields = ['rut','name','correo','fono','direccion']