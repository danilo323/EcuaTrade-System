from src.infrastructure.sqlite_repository import clsSQLiteRepository #importamos la base de datos
from src.application.register_user import ClsRegisterUser #importamos la funcion general de filtrar datos
import os#Limpiar consola



#PARA LIMPIAR LA CONSOLA CADA VEZ
def Fnc_limpiar_pantalla():
    """solamente es limpiar la pantalla xd"""
    os.system('cls')

#VISTA DEL MENU PRINCIPAL PERO SE LLAMARA EN LA FNC PRINCIPAL
#el menu que se mostrara con diseño simple
def Fnc_mostrar_menu():
    """Dibuja la interfaz para el usuario."""
    print("\n" + "="*45)
    print("  ECUATRADE - SISTEMA PRINCIPAL ")
    print("="*45)
    print("  [1] Registrar Nuevo Usuario")
    print("  [2] Buscar usuario por cedula")
    print("  [3] Mostrar todos los Usuarios")
    print("  [4] Actualizar Usuarios")
    print("  [5] Eliminar Usuarios")
    print("  [6] Salir del Sistema")

    print("="*45)
    return input("Elige una opción (1 al 6): ")#devolver el valor atrapado fnc_iniciar



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



'''FUNCION PRINCIPAL QUE LLAMA A TODAS LAS DEMAS'''
#iniciar sistema
def Fnc_iniciar_sistema():
     #definimos la base de datos lista
    motor_sqlite= clsSQLiteRepository()
    sistema_registro= ClsRegisterUser(repository=motor_sqlite)

    while True:
        Fnc_limpiar_pantalla()
        option_escoger=Fnc_mostrar_menu()

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




if __name__=="__main__": Fnc_iniciar_sistema()#llamamos para hacer la prueba CONSTRUCTOR
