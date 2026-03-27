'''Configuración de la base de datos exclusiva para los Productos/Periféricos'''
import sqlite3
import os
import logging

# Configuramos los mensajes de sistema
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

class clsProductSQLiteRepository:
    def __init__(self, db_name="ecuatrade.db"):
        # Usamos LA MISMA base de datos que los usuarios (ecuatrade.db)
        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        self.db_path = os.path.join(base_dir, db_name)
        self._create_table()

    def _get_connection(self) -> sqlite3.Connection:
        """Abre la conexión y permite leer los datos como diccionarios."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row 
        return conn

    def _create_table(self):
        """Crea la tabla de productos si no existe."""
        try:
            with self._get_connection() as conn:
                # Usamos AUTOINCREMENT para que el ID del producto se genere solo (1, 2, 3...)
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS productos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre_producto TEXT NOT NULL,
                        precio REAL NOT NULL
                    )
                """)
            logging.info("Tabla 'productos' inicializada correctamente.")
        except sqlite3.Error as e:
            logging.error(f"Error crítico al crear la tabla productos: {e}")

    def Fnc_Guardar_producto_db(self, product_data) -> bool:
        """Guarda un nuevo producto en la base de datos."""
        query = "INSERT INTO productos (nombre_producto, precio) VALUES (?, ?)"
        
        try:
            with self._get_connection() as conn:
                # Extraemos los datos del diccionario que armaste en application
                conn.execute(query, (
                    product_data["Nombre_producto"], 
                    product_data["precio"]
                ))
            logging.info(f"✅ Producto '{product_data['Nombre_producto']}' guardado con éxito.")
            return True
        except sqlite3.Error as e:
            logging.error(f"❌ Error interno al guardar producto: {e}")
            return False
        
    def Fnc_obtener_todos_los_productos(self):
        """Devuelve una lista con todos los productos de la tienda (Para ver el catálogo)."""
        query = "SELECT * FROM productos"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query)
                # Convertimos cada fila en un diccionario para que sea fácil de leer en tu main.py
                return [dict(row) for row in cursor.fetchall()] 
        except sqlite3.Error as e:
            logging.error(f"Error al leer el catálogo: {e}")
            return [] # Devuelve lista vacía si falla

    def Fnc_actualizar_producto(self, id_producto: int, nuevo_nombre: str, nuevo_precio: float) -> bool:
        """Actualiza el nombre y precio de un producto usando su ID (Para el vendedor)."""
        query = "UPDATE productos SET nombre_producto = ?, precio = ? WHERE id = ?"
        try:
            with self._get_connection() as conn:
                # Ojo: Aquí le pasamos el ID al final porque así está en el WHERE
                cursor = conn.execute(query, (nuevo_nombre.strip().title(), nuevo_precio, id_producto))
                
                if cursor.rowcount > 0:
                    logging.info(f"✅ Producto ID {id_producto} actualizado correctamente.")
                    return True
                else:
                    logging.warning(f"⚠️ No se encontró el producto con ID {id_producto}.")
                    return False
        except sqlite3.Error as e:
            logging.error(f"❌ Error al actualizar en SQLite: {e}")
            return False

    def Fnc_eliminar_producto(self, id_producto: int) -> bool:
        """Elimina un producto de la base de datos permanentemente."""
        query = "DELETE FROM productos WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query, (id_producto,))
                if cursor.rowcount > 0:
                    logging.info(f"🗑️ Producto ID {id_producto} eliminado.")
                    return True
                else:
                    logging.warning(f"⚠️ No se encontró el producto con ID {id_producto} para eliminar.")
                    return False
        except sqlite3.Error as e:
            logging.error(f"❌ Error al eliminar en SQLite: {e}")
            return False
        
    def Fnc_buscar_producto_por_id(self, id_producto: int):
        """Busca un solo producto por su ID y lo devuelve como diccionario."""
        query = "SELECT * FROM productos WHERE id = ?"
        try:
            with self._get_connection() as conn:
                cursor = conn.execute(query, (id_producto,))
                row = cursor.fetchone()
                if row:
                    return dict(row) # Lo convertimos en diccionario
                return None # Si no existe, devolvemos nada
        except sqlite3.Error as e:
            logging.error(f"Error al buscar el producto con ID {id_producto}: {e}")
            return None