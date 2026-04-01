from django.db import models

# Importamos tus validadores recién creados
from .validators import validar_precio_producto, validar_nombre_producto, validar_stock_producto #ruta

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
    
    def __str__(self):
        return self.nombre_producto #no constructor identificacion del objecto
    



    


    
