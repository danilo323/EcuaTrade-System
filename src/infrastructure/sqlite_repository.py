'''Configuracion completa de la base de datos'''
import sqlite3
import os
import logging

# Configuramos los mensajes de sistema 
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class clsSQLiteRepository:
    def __init__(self, db_name="ecuatrade.db"):
        # Esto asegura que la DB siempre se guarde en la carpeta principal de tu proyecto
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.db_path = os.path.join(base_dir, db_name)
        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Abre la conexión y permite leer los datos como diccionarios."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row # Magia pura: permite usar resultado['nombre']
        return conn

    def _create_table(self):
        """Crea la estructura de la tabla de forma segura."""
        try:
            with self._get_connection() as conn:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS usuarios (
                        cedula TEXT PRIMARY KEY,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        correo TEXT UNIQUE NOT NULL
                    )
                """)
            logging.info("Base de datos SQLite inicializada correctamente.")
        except sqlite3.Error as e:
            logging.error(f"Error crítico al crear la tabla: {e}")

    def Fnc_Guardar_registro(self, usuario) -> bool:
        """Guarda un usuario  evitando errores de duplicados."""
        #corregimos para mostrar correcatemtne el diccionario de datos 
        cedula_limpia = usuario["cedula"]
        nombre_limpio = usuario["nombre"]
        apellido_limpio = usuario["apellido"]
        email_limpio = usuario["correo"] 

        query = "INSERT INTO usuarios (cedula, nombre, apellido, correo) VALUES (?, ?, ?, ?)"
        try:
            with self._get_connection() as conn:
                conn.execute(query, (cedula_limpia, nombre_limpio, apellido_limpio, email_limpio))                # El bloque 'with' hace el commit automáticamente, muy Clean Code.
            return True
        except sqlite3.IntegrityError:
            logging.warning(f"Rechazado: La cédula {cedula_limpia} o el email ya existen en el sistema.")
            return False
        except sqlite3.Error as e:
            logging.error(f"Error interno al guardar: {e}")
            return False

    def buscar_por_cedula(self, cedula: str):
        """Busca un usuario y devuelve un diccionario con sus datos."""
        query = "SELECT * FROM usuarios WHERE cedula = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query, (cedula,))
                row = cursor.fetchone()
                if row:
                    return dict(row) # Lo convertimos a diccionario para usarlo fácil
                return None
        except sqlite3.Error as e:
            logging.error(f"Error al buscar cédula {cedula}: {e}")
            return None
        
    def Fnc_actualizar_usuario(self, cedula: str, new_nombre:str, new_apellido:str, new_email:str) -> bool:

        #definir parametros de defensa
        new_nombre= new_nombre.strip().title()
        new_apellido=new_apellido.strip().title()
        new_email=new_email.lower().strip()

        query= '''
                UPDATE usuarios
                SET NOMBRE= ?, apellido= ?, correo= ?
                WHERE cedula= ?
        '''

        try:
            with self._get_connection() as conn:
                cursor= conn.execute(query, (new_nombre, new_apellido, new_email, cedula.strip()))
                if cursor.rowcount>0:
                    logging.info(f"Datos de la cedula {cedula} actualizadas correctamente")
                    return True
                else:
                    logging.info(f"no se econtro el usario con la cedula {cedula} para actualizar.")
                    return False

        except sqlite3.Error as e:
            logging.error(f"error al actualizar en Sqlite3: {e}")
            return False
        
    def Fnc_obtener_todos_los_usuarios(self):
        query = "SELECT * FROM usuarios"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query)
                return cursor.fetchall() # ¡Esto devuelve una lista con todos!
        except sqlite3.Error as e:
            print(f"Error al leer la base de datos: {e}")
            return [] # Devuelve una lista vacía si hay error
        

    def Fnc_eliminar_usuario(self, cedula: str) -> bool:
        """Elimina un usuario de la base de datos permanentemente."""
        query = "DELETE FROM usuarios WHERE cedula = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query, (cedula.strip(),))
                if cursor.rowcount > 0:
                    logging.info(f"Usuario con cédula {cedula} eliminado.")
                    return True
                else:
                    logging.warning(f"No se encontró la cédula {cedula} para eliminar.")
                    return False
        except sqlite3.Error as e:
            logging.error(f"Error al eliminar en SQLite: {e}")
            return False