'''(PRUEBA)
base de datos temporal solo sirve para comprobar duplicados (cedula, correo) NO USANDO MYSQLE3'''

class clsMemoryRepository:
    def __init__(self):
        
        #lista temporal para guardar
        self.users=[]

    def Save(self,user_data:dict):
        
        """recibe un diccionario con parametro: nombre, apellido, cedula, correo
         y verificar que no esten duplicados"""
        

        #1 buscador
        for u in self.users:
            if u['cedula']== user_data['cedula']:
                print(f'error la cedula {user_data["cedula"]} ya esta registrada')
                return False
            
        
            if u['correo'].lower() == user_data['correo'].lower():
                print(f'error el correo {user_data["correo"].lower()} ya esta registrado ')
                return False
    
    #2 guardar si no existen registrados

        self.users.append(user_data)
        print(f"\n Usuario {user_data["nombre"]} guardado con éxito ")
        return True
    



if __name__ == "__main__":
    # 1. Creamos la base de datos de mentira
    repo = clsMemoryRepository()
    
    # 2. Creamos dos usuarios con la MISMA CÉDULA para probar
    usuario_1 = {
        "nombre": "Danilo", 
        "apellido": "Angulo", 
        "correo": "daly@mail.com", 
        "cedula": "1207969013"
    }
    
    usuario_2 = {
        "nombre": "Andy", 
        "apellido": "Tamayo", 
        "correo": "andy@mail.com", 
        "cedula": "1207969013"  # <--- ¡Misma cédula que Danilo!
    }

    print("--- Intentando primer registro ---")
    repo.Save(usuario_1) # Este debe decir: Guardado con éxito

    print("\n--- Intentando segundo registro (Duplicado) ---")
    repo.Save(usuario_2) # Este debe decir: Error la cedula ya esta registrada