'''Cerebro usamos la fnc cedula para decidir guardar el usuario'''
from src.domain.validators import Fncvalidate_cedula, Fncvalidate_mail, Fncvalidate_name

class ClsRegisterUser:
    def __init__(self, repository):
        # Aquí recibimos la base de datos (puerto)
        self.repository = repository
    #aqui executamos todas las funciones de validator. en el orden establecido muy importante
    def Fnc_Procesar_registro(self, nombre: str, apellido: str, correo: str, cedula: str ):
        """Proceso para registrar un nuevo vendedor o comprador"""
        
        #Validamos la cédula con tu lógica de Ecuador
        if not Fncvalidate_cedula(cedula):
            print(f"Error: La cédula {cedula} no es valida.")
            return False
        
        #validacion del nombre y apellido
        if not Fncvalidate_mail(correo):
            print(f"error: el correo {correo} no es valido. ")
            return False
        
        if not Fncvalidate_name(nombre,apellido):
            print(f'error el {nombre} y el {apellido} no son validos.')
            return False

        #Preparamos el diccionario de datos para mandarlos a sqlite3 y limpiados
        user_data = {
            "nombre": nombre.strip().title(),
            "apellido": apellido.strip().title(),
            "correo": correo.strip().lower(),
            "cedula": cedula.strip()
        }

        # 3. Guardamos (en SQLite)
        verificar_guardar= self.repository.Fnc_Guardar_registro(user_data)

        #mandar en el main para verificar el registrado
        if verificar_guardar == True:
            print(f"¡Usuario {nombre} registrado con éxito!")
            return True
        elif verificar_guardar == False:
            print(f'Error: usuario {nombre} no se ha registrado...')