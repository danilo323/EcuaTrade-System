
'''(TEMPORAL)Simulamos la Base de Datos temporal antes de usa mysqlite3 
''''''manejada para en formato de inpuns'''
'''vinculada a memory_repository.py'''
from src.domain.validators import Fncvalidate_cedula, Fncvalidate_mail, Fncvalidate_name
from src.application.register_user import RegisterUser

class MemoryRepository:
    def __init__(self):
        self.users = []

    def save(self, user_data):
        self.users.append(user_data)
        print(f"--- Guardado en BD: {user_data} ---")

# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    repo = MemoryRepository() #unioin a memory_repository
    cerebro = RegisterUser(repo)

    print("--- REGISTRO DE MARKETPLACE ---")
    n = input("Nombre: ")
    a = input("Apellido: ")
    c = input("Correo: ")
    ced = input("Cédula: ")

    if cerebro.execute(n, a, c, ced):
        print("\nLista de usuarios en BD:", repo.users)