def validar(numero):                            #Recibe el número como string
    cantidad = len(numero)
    if(cantidad > 0):
        if(numero[0] in "-+" and cantidad > 1): #Retira el signo si comienza con uno 
            numero = numero[1:]
            cantidad -= 1
        punto = False                           #Bandera que verifica si el número tiene punto
        digitos = "0123456789"
        for i in range(cantidad):
            if(numero[i] in digitos):           #Compara cada caracter con los dígitos del 0 al 9
                continue
            elif(numero[i] == "." and i > 0):   #Busca si el caracter actual es un punto
                if(not punto):                  #Verifica que el número no tenga más de un punto
                    punto = True
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

def esPrimo(num):
    if(num >= 2):
        for i in range(2, int(num**0.5) + 1):
            if(num%i == 0):
                return False
        return True
    else:
        return False