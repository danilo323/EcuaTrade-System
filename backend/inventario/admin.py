from django.contrib import admin
from .models import Categoria, Producto, ProductoImagen, Variante

# 1. Registramos la categoría de forma sencilla
admin.site.register(Categoria)

# 2. Truco Senior: Inlines (Para agregar fotos y variantes DENTRO del producto)
class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1 # Te deja una fila vacía lista para subir una foto

class VarianteInline(admin.TabularInline):
    model = Variante
    extra = 1 # Te deja una fila vacía lista para agregar un color/tamaño

# 3. Configuramos la vista principal del Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # Columnas que verás en la tabla general
    list_display = ('nombre_producto', 'precio', 'stock', 'categoria', 'badge')
    # Filtros a la derecha de la pantalla
    list_filter = ('categoria', 'vendedor')
    # Barra de búsqueda
    search_fields = ('nombre_producto',)
    # Aquí inyectamos las fotos y variantes
    inlines = [ProductoImagenInline, VarianteInline]