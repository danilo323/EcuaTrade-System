#Migracion mandar src 
#mtermeos las validaciones de productos anteriormente

from django.core.exceptions import ValidationError

def validar_nombre_producto(value):

    Nombre_producto_limpio=value.strip()

    if len(Nombre_producto_limpio) ==0 :
        raise ValidationError("Erro: campo vacio ")
      
    if len(Nombre_producto_limpio) >50:
        raise ValidationError("Error: campo lleno") 


def validar_precio_producto(value):
    
    if value <=0:
        raise ValidationError("Error: El precio debe ser mayor a 0")


def validar_stock_producto(value):

    if value <=0:
        raise ValidationError("Error: El stock debe ser mayor a 0")



    

