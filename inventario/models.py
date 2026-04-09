from django.db import models
# Importamos tus validadores recién creados
from .validators import validar_precio_producto, validar_nombre_producto, validar_stock_producto #ruta

#accemos importancion del usuario para vincularlo con el vendedor
from django.conf import settings
#autenticacion de roles de usuarios
from django.conf import settings


'''Validaciones de producto para la creacion de base de datos'''

#models.Model= creacion de base de datos  a django 
#gracias a eso a diferencia de SRC no se abrira conexiones con sqlite3 manualmente

class Producto(models.Model):
    nombre_producto = models.CharField( #charfied =tipo Var
        max_length=150, 
        validators=[validar_nombre_producto] # Conectado
    )
    precio = models.DecimalField(
        max_digits=10,  
        decimal_places=2, 
        validators=[validar_precio_producto] # Conectado
    )  

    '''Aun no tiene validor'''
    stock = models.IntegerField(
        default=0,#numeros enteros, por defecto sin precio a cero 
        validators=[validar_stock_producto]
    )

    '''conexion para el usuario  '''
    vendedor= models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='productos',
        default=1 #definir en defualt para productos que quedaron en blanco en las pruebas

    )

    #especificacion de orl de usuario
    vendedor = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='productos'
    )

    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)

    #especificacion de usuario



    def __str__(self):
        return self.nombre_producto #no constructor identificacion del objecto
    



    


    
