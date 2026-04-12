from rest_framework import serializers
from .models import Producto, Categoria, ProductoImagen, Variante

# 1. TRADUCTOR DE CATEGORÍAS
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

# 2. TRADUCTOR DE IMÁGENES EXTRA
class ProductoImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoImagen
        fields = ['id', 'imagen', 'es_principal']

# 3. TRADUCTOR DE VARIANTES (RAM, Color, etc.)
class VarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variante
        fields = ['id', 'nombre', 'opcion', 'stock_variante', 'imagen_asociada']

# 4. TRADUCTOR MAESTRO (Producto)
class ProductoSerializer(serializers.ModelSerializer):
    vendedor = serializers.ReadOnlyField(source='vendedor.username')
    categoria_detalle = CategoriaSerializer(source='categoria', read_only=True)
    # Añadimos esto para asegurar que el formulario de DRF muestre el dropdown
    categoria = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all())
    imagenes = ProductoImagenSerializer(many=True, read_only=True)
    variantes = VarianteSerializer(many=True, read_only=True)
    badge = serializers.ReadOnlyField()

    class Meta:
        model = Producto
        fields = [
            'id', 'vendedor', 'nombre_producto', 'precio', 'stock', 
            'imagen', 'categoria', 'categoria_detalle', 
            'imagenes', 'variantes', 'badge', 'ventas_totales'
        ]