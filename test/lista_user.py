('''ver de manera temormal en la base de datos los usuarios no en el main''')
from src.infrastructure.sqlite_repository import clsSQLiteRepository

def ver_registrados():
    repo = clsSQLiteRepository()
    
    # Vamos a usar una consulta manual para ver a todos
    print("📋 LISTA DE USUARIOS EN ECUATRADE-SYSTEM")
    print("-" * 40)
    
    with repo._get_connection() as conn:
        cursor = conn.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        
        if not usuarios:
            print("La base de datos está vacía.")
        else:
            for u in usuarios:
                # Como usamos el 'Modo Pro' (sqlite3.Row), 
                # puedes acceder por nombre de columna:
                print(f"ID: {u['cedula']} | Nombre: {u['nombre']} {u['apellido']} | Email: {u['email']}")
    
    print("-" * 40)

if __name__ == "__main__":
    ver_registrados()