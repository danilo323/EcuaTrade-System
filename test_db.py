from src.infrastructure.sqlite_repository import clsSQLiteRepository
'''sandboxing= entorno de pruebas para probar mi base de datos '''
# Objeto simulado
class UserMock:
    def __init__(self, cedula, first_name, last_name, email):
        self.cedula = cedula
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

def ejecutar_prueba():
    print("🚀 Iniciando Test de Persistencia de EcuaTrade-System...\n")
    repo = clsSQLiteRepository()
    
    # 1. Creamos a los usuarios en memoria
    daly = UserMock("1200000000", "Danilo", "Angulo", "daly@ecuatrade.com")
    yulexi = UserMock("1207969013", "Yulexi", "Nuñes", "yule14@hotmail.com")
    manuel = UserMock("0999999999", "  jOaN", "  pErEz", "  joan_nuevo@mail.com ")
    # 2. Intentamos Guardar
    print("--- Fase 1: Guardado de Datos ---")
    
    # Le damos la orden explícita de guardar a Daly
    if repo.guardar(daly):
        print(f"✅ Éxito: Usuario {daly.first_name} guardado en disco duro.")
    else:
        print(f"⚠️ Nota: El usuario {daly.first_name} no se guardó (ya existe).")
        
    # LE DAMOS LA ORDEN EXPLÍCITA DE GUARDAR A YULEXI (Esto faltaba)
    if repo.guardar(yulexi):
        print(f"✅ Éxito: Usuario {yulexi.first_name} guardada en disco duro.")
    else:
        print(f"⚠️ Nota: La usuaria {yulexi.first_name} no se guardó (ya existe).")

    if repo.guardar(manuel):
        print(f'Éxito: Usuario {manuel.first_name} guardado en disco duro.')
    else:
        print(f'⚠️ Nota: La usuaria {manuel.first_name} no se guardó (ya existe).')    
    
    # 3. Intentamos Buscar
    print("\n--- Fase 2: Recuperación de Datos ---")
    
    # Buscamos a Yulexi para confirmar que sí entró a la base de datos
    resultado = repo.buscar_por_cedula("1207969013")
    
    if resultado:
        print(f"🔍 Encontrado en Base de Datos:")
        print(f"   - Nombre completo: {resultado['nombre']} {resultado['apellido']}")
        print(f"   - Correo asociado: {resultado['email']}")
    else:
        print("❌ Falla: Usuario no encontrado.")

if __name__ == "__main__":
    ejecutar_prueba()