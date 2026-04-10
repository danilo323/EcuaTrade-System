from rest_framework import serializers #llamamos a la tecnologia rest_frmowekr aqui
from .models import Producto #para especificar quew datos vamos a convertir a json, q se traduce


'''transformar a sqlite a formato JSON PARA REACT'''

class ProductoSerializer(serializers.ModelSerializer):
    # Hacemos que el vendedor sea de solo lectura
    # Además, mostramos el nombre del usuario en lugar de solo el ID
    vendedor = serializers.ReadOnlyField(source='vendedor.username')

    class Meta:
        model = Producto
        fields = ['id', 'nombre_producto', 'precio', 'stock', 'imagen', 'vendedor']
    class Meta:
        model = Producto
        fields = '__all__' # Esto significa: "Traduce todas las columnas de la tabla"