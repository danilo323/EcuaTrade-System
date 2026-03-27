# --- ESTAS 3 LÍNEAS ARREGLAN EL ERROR DEL CMD ---
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# ------------------------------------------------

'''Usaremos products_validators para las funciones para hacer el registro de equipo'''
from src.domain.products_validators import Fnc_validar_nombre_producto, Fnc_Validar_precio_producto

class ClsRegisterProducts:
    def __init__(self, repository):
        self.repository = repository

    def Fnc_procesar_registro_productos(self, precio, Nombre_producto: str):
        '''Proceso para registrar productos'''

        if not Fnc_Validar_precio_producto(precio):
            print('Error: no ha sido ingresado correctamente el precio')
            return False
        
        if not Fnc_validar_nombre_producto(Nombre_producto):
            print('Error: no ha sido valido el nombre del producto')
            return False
        
        user_data = {
            "precio": precio,
            "Nombre_producto": Nombre_producto.strip().title()
        }

        # Guardar en sqlite3 (usando el nombre correcto Fnc_Guardar_producto_db)
        verificar_producto_guardado = self.repository.Fnc_Guardar_producto_db(user_data)

        # Verificar si está registrado
        if verificar_producto_guardado == True:
            print(f'Se ha guardado correctamente, el producto {user_data["Nombre_producto"]} ya esta en la tienda.')
            return True
        elif verificar_producto_guardado == False:
            return False

