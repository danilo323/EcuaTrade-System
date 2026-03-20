'''Cerebro usamos la fnc cedula para decidir guardar el usuario'''
from src.domain.validators import Fncvalidate_cedula, Fncvalidate_mail, Fncvalidate_name

class RegisterUser:
    def __init__(self, repository):
        # Aquí recibimos la base de datos (puerto)
        self.repository = repository

    def execute(self, nombre: str, apellido: str, correo: str, cedula: str ):
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

        #Preparamos el diccionario de datos
        user_data = {
            "nombre": nombre.strip().title(),
            "apellido": apellido.strip().title(),
            "correo": correo.strip().lower(),
            "cedula": cedula.strip()
        }

        # 3. Guardamos (hoy en memoria, mañana en SQLite)
        self.repository.save(user_data)
        print(f"✅ ¡Usuario {nombre} registrado con éxito!")
        return True