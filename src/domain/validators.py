
'''validacion si la cedula es ecuatoriana o no dependiendo de los 10 digitos'''
def Fncvalidate_cedula(cedula:str):
    #array a cedula para validar digitos

    #verificar que solo sea digito
    if not cedula.isdigit():
        print("Error: la cedula dbee contener solo numeros (0-9)")
        return False

        #verificar longitud
    if len(cedula) !=10:
        print("cedula presenta 10 caracteres")
        return False
    

    
    
    #esocogemos los primeros digitos 
    #primer 1 y 2 digitos provincia
    array_digitoProvincia=int(cedula[0:2])
    
    if array_digitoProvincia < 1 or array_digitoProvincia >24:
        print("la cedula no es ecuatoriana")
        return False

    #distincio de persona
    #regla 3 digito =persona natural >5
    #regla 6 digito =institucion
    #regla 9 digito = extranjera

    array_personaNtural=int(cedula[2])

    if array_personaNtural > 5:
        print("cedula natural invalidad")
        return False
    

    suma_total = 0
    # Usamos un rango del 0 al 8 (los primeros 9 dígitos)
    for i in range(9):
        valor = int(cedula[i])
        if i % 2 == 0: # Posiciones 0, 2, 4, 6, 8
            valor = valor * 2
            if valor > 9:
                valor -= 9
        
        suma_total += valor

    # 1. Calculamos el residuo
    residuo = suma_total % 10

    # 2. Tu lógica para el dígito verificador
    if residuo == 0:
        digito_verificador = 0
    else:
        digito_verificador = 10 - residuo

    # 3. Comparación final (Ojo: convierte el último dígito a int)
    if digito_verificador == int(cedula[9]):
        print("Cédula válida. ¡Bienvenido al Marketplace!")
        return True
    else:
        print("El décimo dígito no coincide. Cédula falsa.")
        return False




def Fncvalidate_name(nombre,apellido):

    nombre=nombre.strip()
    apellido=apellido.strip()
    
    if len(nombre) == 0 or len(nombre) >=30:
        
        print("Error: el nombre debe de tener entre 1 y 29 caracteres. ")
        return False

    if len(apellido) ==0 or len(apellido) >=30:  
        print("Error: el Apelliso debe de tener entre 1 y 29 caracteres.")
        return False
    
    else:
        print(f'Correcto: Nombres: {nombre} y {apellido} correctamente.')
        return True


def Fncvalidate_mail(correo: str):

    correo=correo.strip().lower()
    
    #buscar las posiciones
    ultimo_punto=correo.rfind(".")

     #que no supere el estandar de maximo caracteres posible
    if len(correo) > 254:
        print("maximo de caracteres permitidos!")
        return False

    #verificar donde se ecuentra el "@"
    if correo.startswith("@") or correo.endswith("@"):
        print("error: posicion @ no valida ")
        return False
    
    #verificar que tenga 2 caracteres estrictamente especiales
    if "@" not in correo or "." not in correo:
        print("el correo debe tener un dominio '@' y dominio .")
        return False

    #validar que tenga al menos un caracter
    if len(correo)== 0 or " " in correo:
        print("No dejes espacios en blanco! ")
        return False

    #verificar que el . no sea el ultimo digito
    if ultimo_punto == -1 or ultimo_punto == len(correo) - 1:
        print("Error: El dominio no es válido (ejemplo: .com)")
        return False

    # 3. Validamos que el punto este despues de @
    if ultimo_punto < correo.find("@"):
        print("Error: El punto debe estar después del @")
        return False
    
    if correo.find("@") + 1 == ultimo_punto:
        print("Error: El dominio no puede estar vacío (ejemplo: @gmail.com)")
        return False
    
    return True


   

#verificador de correo
#if __name__=="__main__":

#    correo_user=input("ingrese su correo: ")
#    resultado=Fncvalidate_mail(correo_user)

#    if resultado:

#        print("correcto")
#    else:
#        print("error en el correo ")


# if __name__=="__main__":

#     name_user=input("ingrese su nombre").strip('" "')
#     lastname_user=input("ingrese su apellido").strip('" "')

#     result=Fncvalidate_name(name_user,lastname_user)

#     if result:
#         print("Funciono")
    
#     else:
#         print("error 404")




    #VALIDAR CEDULA

#if __name__=="__main__":

  #  mi_cedula= input("ingresar cedula a probar: ")
   # resultado= Fncvalidate_cedula(mi_cedula)


    #if resultado:
     #   print("FUNCIONA LA CEDULDA")
    #else:
     #   print("ERROR 404")