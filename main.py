from src.infrastructure.sqlite_repository import clsSQLiteRepository #importamos la base de datos (USUARIOS)
from src.infrastructure.sqlite_repository_products import clsProductSQLiteRepository
from src.application.register_user import ClsRegisterUser #importamos la funcion general de filtrar datos ysuarios
from src.application.register_products import ClsRegisterProducts#las funciones de filtrar los productos
import os#Limpiar consola



#PARA LIMPIAR LA CONSOLA CADA VEZ
def Fnc_limpiar_pantalla():
    """solamente es limpiar la pantalla xd"""
    os.system('cls')


'''FUNCIONES CRUD DE USUARIOS'''
'''[U][S][U][A][R][I][O][S]'''

def Fnc_mostrar_menu_usuarios():
    """Dibuja la interfaz para el usuario."""
    print("\n" + "="*45)
    print("  ECUATRADE - SISTEMA PRINCIPAL ")
    print("="*45)
    print("  [1] Registrar Nuevo Usuario")
    print("  [2] Buscar usuario por cedula")
    print("  [3] Mostrar todos los Usuarios")
    print("  [4] Actualizar Usuarios")
    print("  [5] Eliminar Usuarios (Especifico)")
    print("  [6] Salir del Sistema")

    print("="*45)
    return input("Elige una opción (1 al 6): ")#devolver el valor atrapado fnc_iniciar



'''FUNCION PRINCIPAL DEL USUARIO'''
#iniciar sistema
def Fnc_iniciar_sistema_usuarios():
     #definimos la base de datos lista
    motor_sqlite= clsSQLiteRepository()
    sistema_registro= ClsRegisterUser(repository=motor_sqlite)

    while True:
        Fnc_limpiar_pantalla()
        option_escoger=Fnc_mostrar_menu_usuarios()

        if option_escoger=="1":
            Fnc_registrar_usuarios(sistema_registro)#REGISTRA USUARIOS
            input("presione Enter para regresar en el menu")

        elif option_escoger =="2":
            Fnc_buscar_usuario_por_cedula(motor_sqlite)#BUSCA USAURIOS
            input("presione Enter para regresar en el menu")

        elif option_escoger == "3":
            Fnc_usuarios_todos(motor_sqlite)#MUESTRA A TODOS LOS USUARIOS
            input("presione Enter para regresar al menu")

        elif option_escoger== "4":
            Fnc_actualizar_los_usuarios(motor_sqlite)#ACTUALIZA A TODOS LOS USUARIOS
            input("presione Enter para regresar al menu")

        elif option_escoger== "5":
            Fnc_borrar_usuario(motor_sqlite)#BORRAR USUARIO POR COMPLETOA
            input("presione Enter para regresar al menu")
        
        elif option_escoger =="6":#SALIR DEL SISTEMA
            print("saliendo del sistema...")
            print("Ha salido del sistema!.")
            break
                
        else:# SI SE PRESIONA OTRO VALOR POR ERROR
            print("opcion invalida intente de nuevo: ")
            input("presione cualquier boton... ")
        
    pass


def Fnc_registrar_usuarios(sistema_registro):
    #definimos la base de datos lista
  
    print("entrando al sistema")
    nombre_ingresar=input("ingrese su nombre: ")
    apellido_ingresar=input("ingrese su apellido: ")
    correo_ingresar=input("ingrese su correo: ")
    cedula_ingresar=input("ingrese su cedula: ")

    #llamamos a la variable y buscamo la fnc Fnc_Procesar_registro 
    sistema_registro.Fnc_Procesar_registro(nombre_ingresar, apellido_ingresar, correo_ingresar, cedula_ingresar)

'''ACTUALIZAR LOS USUARIOS'''
def Fnc_actualizar_los_usuarios(motor_sqlite):
    cedula_buscar=input("ingrese la cedula para buscar: ")
    resultado= motor_sqlite.buscar_por_cedula(cedula_buscar)

    '''verificar si la cedula existe'''
    if resultado:
        #pedir el cambio de datos 
        nombre_ingresar=input("ingrese su nombre: ")
        apellido_ingresar=input("ingrese su apellido: ")
        correo_ingresar=input("ingrese su correo: ")
        
        '''mandar a los datos a la fnc de miqsqlite3 (actualizar)'''
        motor_sqlite.Fnc_actualizar_usuario(cedula_buscar, nombre_ingresar, apellido_ingresar, correo_ingresar)
        print("Informacion actualizada con exito!")

    #verificar que la cedula si exista 
    else:

        print("no se econtro la cedula en la base de datos")

'''buscar usuario por la cedula'''
def Fnc_buscar_usuario_por_cedula(motor_sqlite):
    cedula_buscar=input("ingrese la cedula para buscar: ")#la entrada
    resultado=motor_sqlite.buscar_por_cedula(cedula_buscar)#el resultado y a que funcion estaremos usando en mysql.py y comparnadole con el input de buscar

    if resultado: #especifacamos que buscamos 
        print(f"Nombre del cliente: {resultado['nombre']}, Apellido del cliente: {resultado['apellido']} ")
        print(f"Correo del cliente {resultado['correo']}")
        
    else:
        print(f'no se econtro la cedula en la base de datos')#si no hay ninugn usario 
        
'''Mostrar todos los usuarios'''
def Fnc_usuarios_todos(motor_sqlite):
    lista_usuarios = motor_sqlite.Fnc_obtener_todos_los_usuarios()

    if not lista_usuarios:
        print(f'Error: no hay ningún usuario registrado en la base')
        return # Salimos para no seguir ejecutando

    # Primero imprimimos la cabecera
    print("\n" + "=" * 60)
    print(f"      📋 LISTADO COMPLETO ({len(lista_usuarios)} usuarios)")
    print("=" * 60)

    for usuario in lista_usuarios: # 'usuario' es el individual, 'lista_usuarios' el grupo
        print(f"👤 NOMBRE:   {usuario['nombre']} {usuario['apellido']}")
        print(f"🆔 CÉDULA:   {usuario['cedula']}")
        print(f"📧 CORREO:   {usuario['correo']}")
        print("-" * 40)

    print("=" * 60 + "\n")


#Funcion para borrar
def Fnc_borrar_usuario(motor_sqlite):
    cedula_buscar=input("ingrese la cedula: ")
    resultado=motor_sqlite.buscar_por_cedula(cedula_buscar)

    if resultado:

        confirmar=input("estas seguro de borrar el usuario S/N").upper()

        if confirmar == 'S':
            motor_sqlite.Fnc_eliminar_usuario(cedula_buscar)
            print("Usario eliminado!")

        else:
            print("operacion cancelada")
            input("presione Enter para regresar en el menu")

    else:
        print("Error: cedula no econtrada")



'''FUNCIONES CRUD DE PRODUCTOS'''
'''[P][R][O][D][U][C][T][O][S]'''


def Fnc_mostrar_menu_productos():
    '''interfaz del menu de productos'''
    print("\n" + "="*45)
    print("  ECUATRADE - SISTEMA DE PRODUCTOS ")
    print("="*45)
    print("  [1] Registrar Nuevo Producto")
    print("  [2] Buscar Producto")
    print("  [3] Mostrar todos los Productos ")
    print("  [4] Actualizar Producto")
    print("  [5] Eliminar Producto Especifico")
    print("  [6] Salir del Sistema")

    print("="*45)

    return input("ingrese una opcion (1 al 6): ")

def Fnc_iniciar_sistema_productos():
    motor_sqlite= clsProductSQLiteRepository()
    sistema_registro_producto= ClsRegisterProducts(repository=motor_sqlite)
    
    
    while True:
        Fnc_limpiar_pantalla()
        opcion_escoger=Fnc_mostrar_menu_productos()

        if opcion_escoger== "1":
            Fnc_registrar_productos(sistema_registro_producto)
            input("presione Enter para regresar en el menu")

        elif opcion_escoger== "2":
            Fnc_buscar_producto(motor_sqlite)
            input("Presione Enter para regrear en el menu")

        elif opcion_escoger== "3":
            Fnc_mostrar_producto(motor_sqlite)
            input("Presione Enter para regresar en el menu")

        elif opcion_escoger== "4":
            Fnc_actualizar_producto(motor_sqlite)
            input("Presiona Enter para regresar en el menu")            

        elif opcion_escoger== "5":
            Fnc_eliminar_producto(motor_sqlite)
            input("Presione Enter para regresar en el menu")

        elif opcion_escoger=="6":
            print("saliendo del sistema...")
            print("Ha salido del sistema!.")
            break

        else:
            print("Porfavor escoga una opcion valida")




'''Funcion registrar producto'''
def Fnc_registrar_productos(sistema_registro_producto):
      print("Entrando al sistema..")
      Nombre_producto=input("ingrese el nombre del producto: ")
      precio=input("ingrese el precio del producto: ")

      sistema_registro_producto.Fnc_procesar_registro_productos(precio,Nombre_producto)



'''Funcion para buscar producto'''

def Fnc_buscar_producto(motor_sqlite):
    print("\n🔍 Entrando a la base de datos...")
    numero_id = input("Ingrese el ID del producto: ")
    
    try:
        # IMPORTANTE: Convertimos a entero para que SQLite lo reconozca
        id_int = int(numero_id)
        resultado = motor_sqlite.Fnc_buscar_producto_por_id(id_int)

        if resultado:
            print(f"\n✅ PRODUCTO ENCONTRADO:")
            # Usamos emojis para que se vea más moderno en tu consola
            print(f"📦 Nombre: {resultado['nombre_producto']}")
            print(f"💰 Precio: ${resultado['precio']:.2f}")
        else:
            print(f"❌ Error: El ID {id_int} no existe en el sistema.")
            
    except ValueError:
        print("❌ Error: Por favor, ingrese un número de ID válido.")

    

'''Funcion para mostrar todos los productos'''
def Fnc_mostrar_producto(motor_sqlite):
    # Traemos la lista completa
    lista = motor_sqlite.Fnc_obtener_todos_los_productos()
    
    if not lista:
        print("\n⚠️ Error: No hay productos registrados en la base.")
        return

    # Imprimimos una cabecera bonita
    print("\n" + "=" * 55)
    print(f"{'ID':<5} | {'NOMBRE DEL PRODUCTO':<30} | {'PRECIO':<10}")
    print("=" * 55)

    for p in lista:
        # Mostramos los datos alineados
        id_txt = str(p['id']).ljust(5)
        nombre_txt = p['nombre_producto'].ljust(30)
        precio_txt = f"${p['precio']:.2f}"
        print(f"{id_txt} | {nombre_txt} | {precio_txt}")
    
    print("=" * 55 + "\n")


'''Funcion para actualizar los productos'''
def Fnc_actualizar_producto(motor_sqlite):
    print("\n" + "🔄 ACTUALIZAR INFORMACIÓN DE PRODUCTO " + "-"*15)
    # 1. Mostramos la lista para ver qué ID queremos cambiar
    Fnc_mostrar_producto(motor_sqlite)
    
    id_cambiar = input("Ingrese el ID del producto que desea modificar: ")
    
    try:
        id_int = int(id_cambiar)
        # 2. Pedimos los nuevos datos
        nuevo_nombre = input("Ingrese el NUEVO nombre: ")
        nuevo_precio = input("Ingrese el NUEVO precio ($): ")

        # 3. Mandamos al motor de la base de datos
        # Convertimos el precio a float para que SQLite lo guarde bien
        exito = motor_sqlite.Fnc_actualizar_producto(id_int, nuevo_nombre, float(nuevo_precio))

        if exito:
            print(f"✅ ¡Éxito! El producto con ID {id_int} ha sido actualizado.")
        else:
            print(f"⚠️ No se encontró el producto con ID {id_int}.")

    except ValueError:
        print("❌ Error: Datos inválidos. El ID debe ser un número y el precio puede llevar decimales.")

'''Funcion para eliminar producto'''

def Fnc_eliminar_producto(motor_sqlite):
    print("\n" + "🗑️ ELIMINAR PRODUCTO DEL SISTEMA " + "-"*15)
    # Mostramos la lista primero
    Fnc_mostrar_producto(motor_sqlite)
    
    id_borrar = input("Ingrese el ID del producto que desea ELIMINAR: ")

    try:
        id_int = int(id_borrar)
        # 1. Verificamos si existe antes de preguntar (Opcional, pero pro)
        confirmar = input(f"❗ ¿Está seguro de eliminar permanentemente el ID {id_int}? (S/N): ").upper()

        if confirmar == "S":
            # 2. Ejecutamos el borrado
            if motor_sqlite.Fnc_eliminar_producto(id_int):
                print(f"✅ Producto {id_int} eliminado correctamente.")
            else:
                print(f"⚠️ No se pudo eliminar. El ID {id_int} no existe.")
        else:
            print("❌ Operación cancelada por el usuario.")

    except ValueError:
        print("❌ Error: El ID debe ser un número entero.")



#if __name__=="__main__": Fnc_iniciar_sistema_usuarios()#llamamos Sistema de usaurios
if __name__=="__main__": Fnc_iniciar_sistema_productos()#llamamos Sistema de productos
