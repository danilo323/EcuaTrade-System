from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.conf import settings

# Importamos tus validadores
from .validators import validar_precio_producto, validar_nombre_producto, validar_stock_producto


# 1. CATEGORÍAS (Para tu Mega Menú)
from django.db import models

class Categoria(models.Model):
    OPCIONES_CATEGORIA = [
        # Periféricos
        ('MOU', 'Mouse'),
        ('TEC', 'Teclados'),
        ('HEA', 'Headsets'),
        ('MIC', 'Micrófonos'),
        ('WEB', 'Webcams'),
        
        # Componentes
        ('MON', 'Monitores'),
        ('CAS', 'Cases'),
        ('BAS', 'Bases Cooler'),
        ('SOP', 'Soportes'),
        
        # Accesorios
        ('MPA', 'Mouse Pads'),
        ('GAM', 'Gamepads'),
        ('KEY', 'Keycaps'),
        ('SWI', 'Switches'),
        ('FIG', 'Figuras'),
        
        # Gamer & Más
        ('CON', 'Consolas'),
        ('VID', 'Videojuegos'),
        ('SIL', 'Sillas'),
        ('CMB', 'Combos'),
        ('PRO', 'Promociones'),
        
    ]

    nombre = models.CharField(
        max_length=3,
        choices=OPCIONES_CATEGORIA,
        default='OTR',
        unique=True,
        help_text="Selecciona la subcategoría exacta del producto"
    )

    def __str__(self):
        return self.get_nombre_display()

# 2. PRODUCTO PRINCIPAL
class Producto(models.Model):
    nombre_producto = models.CharField( 
        max_length=150, 
        validators=[validar_nombre_producto] 
    )
    precio = models.DecimalField(
        max_digits=10,  
        decimal_places=2, 
        validators=[validar_precio_producto] 
    )  
    stock = models.IntegerField(
        default=0, 
        validators=[validar_stock_producto]
    )

    # Conexión con el Vendedor (Usuario)
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='productos',
        default=1 
    )

    # Conexión con la Categoría (Permitimos nulos temporalmente para que no te dé error con tus productos viejos)
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.SET_NULL, 
        related_name='productos',
        null=True,
        blank=True
    )

    # Imagen principal original
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    
    # Campos automáticos para la lógica de "NEW" y "HOT"
    creado_en = models.DateTimeField(auto_now_add=True)
    ventas_totales = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_producto 

    # El Backend decide qué etiqueta lleva
    @property
    def badge(self):
        if self.creado_en >= timezone.now() - timedelta(days=7):
            return "NEW"
        elif self.ventas_totales >= 50:
            return "HOT"
        return None


# 3. GALERÍA DE IMÁGENES (Para tener más de 1 foto)
class ProductoImagen(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='productos/')
    es_principal = models.BooleanField(default=False)

    def __str__(self):
        return f"Imagen de {self.producto.nombre_producto}"


# 4. VARIANTES DINÁMICAS (Color, RAM, Switch, etc.)
class Variante(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variantes')
    nombre = models.CharField(max_length=50) # Ej: "Color" o "Capacidad"
    opcion = models.CharField(max_length=50) # Ej: "Blanco" o "16GB"
    stock_variante = models.IntegerField(default=0)
    
    # Opcional: Si el vendedor quiere que la variante cambie la foto
    imagen_asociada = models.ForeignKey(ProductoImagen, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.producto.nombre_producto} - {self.nombre}: {self.opcion}"