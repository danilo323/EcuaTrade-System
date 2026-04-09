
from django.core.exceptions import ValidationError

'''validacion si la cedula es ecuatoriana o no dependiendo de los 10 digitos'''
def Fncvalidate_cedula(cedula):
    #array a cedula para validar digitos

    #verificar que solo sea digito
    if not cedula.isdigit():
       raise ValidationError("Error: la cedula debe contener solo numeros (0-9)")
        
        #verificar longitud
    if len(cedula) !=10:
        raise ValidationError("cedula presenta 10 caracteres")
    
    #esocogemos los primeros digitos 
    #primer 1 y 2 digitos provincia
    array_digitoProvincia=int(cedula[0:2])
    
    if array_digitoProvincia < 1 or array_digitoProvincia >24:
        raise ValidationError("la cedula no es ecuatoriana")
        

    #distincio de persona
    #regla 3 digito =persona natural >5
    #regla 6 digito =institucion
    #regla 9 digito = extranjera

    array_personaNtural=int(cedula[2])

    if array_personaNtural > 5:
        raise ValidationError("cedula natural invalidad")
        
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
    if digito_verificador != int(cedula[9]):
      raise ValidationError("El décimo dígito no coincide. Cédula falsa.")




def Fncvalidate_name(nombre,apellido):

    nombre=nombre.strip()
    apellido=apellido.strip()
    
    if len(nombre) == 0 or len(nombre) >=30:
        
        raise ValidationError("Error: el nombre debe de tener entre 1 y 29 caracteres. ")
        

    if len(apellido) ==0 or len(apellido) >=30:  
        raise ValidationError("Error: el Apelliso debe de tener entre 1 y 29 caracteres.")
        
  
        


def Fncvalidate_mail(correo):

    correo=correo.strip().lower()
    
    #buscar las posiciones
    ultimo_punto=correo.rfind(".")

     #que no supere el estandar de maximo caracteres posible
    if len(correo) > 254:
        raise ValidationError("maximo de caracteres permitidos!")
        

    #verificar donde se ecuentra el "@"
    if correo.startswith("@") or correo.endswith("@"):
        raise ValidationError("error: posicion @ no valida ")
        
    
    #verificar que tenga 2 caracteres estrictamente especiales
    if "@" not in correo or "." not in correo:
        raise ValidationError("el correo debe tener un dominio '@' y dominio .")
        

    #validar que tenga al menos un caracter
    if len(correo)== 0 or " " in correo:
        raise ValidationError("No dejes espacios en blanco! ")

    #verificar que el . no sea el ultimo digito
    if ultimo_punto == -1 or ultimo_punto == len(correo) - 1:
        raise ValidationError("Error: El dominio no es válido (ejemplo: .com)")
        

    # 3. Validamos que el punto este despues de @
    if ultimo_punto < correo.find("@"):
        raise ValidationError("Error: El punto debe estar después del @")
        
    
    if correo.find("@") + 1 == ultimo_punto:
        raise ValidationError("Error: El dominio no puede estar vacío (ejemplo: @gmail.com)")
        
    


   

