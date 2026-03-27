def Fnc_Validar_precio_producto(precio:float):
    
    try:
        precio= float(precio)
    except ValueError:
        print("Error el valor debe ser tipo numero ")
        return False
    
    if precio <=0:
        print("error el numero debe ser mayor a 0")
        return False
    
    else:
        print(f'se agrego el producto: valor {precio:.2f}')
        return precio


    

def Fnc_validar_nombre_producto(Nombre_producto:str):

    Nombre_limpio=Nombre_producto.strip()

    if len(Nombre_producto) ==0 :
        print("Error: campo vacio.")
        return False

    if len(Nombre_producto) >50:
        print("Erro: campo lleno")
        return False
    else:
        print(f'Correcto: Nombre {Nombre_limpio} registrado correctamente')
        return Nombre_limpio
    


#if __name__=="__main__":
    
#    Nombre_producto=input("Ingrese el nombre del producto: ")

#    resultado= Fnc_validar_nombre_producto(Nombre_producto)

#    if resultado:
#        print("funciona perfecto:")

#    else:
#        print("error")


#if __name__=="__main__":
#    Precio_producto=input("ingrese el precio del producto: ")
#    resultado=Fnc_Validar_precio_producto(Precio_producto)

#    if resultado:
#        print("correcto")
#     else:
 #       print("error")