# Escriba un programa que pida los coeficientes de una ecuación de primer grado:

# ax + b = 0,
# y que entregue la solución.

# Una ecuación de primer grado puede:

# tener solución única,
# tener infinitas soluciones, o
# no tener soluciones.

from os import system

def validar(numero): #Recibe el número como string
    cantidad = len(numero)
    if(numero[0] == "-" or numero[0] == "+"): #Retira el signo si comienza con uno 
        numero = numero[1:]
        cantidad -= 1
    if(cantidad > 0):
        digitos = "0123456789"
        punto = False #Bandera que verifica si el número tiene punto
        for i in range(cantidad):
            if(numero[i] in digitos): #Compara cada caracter con los dígitos del 0 al 9
                continue
            elif(numero[i] == "." and i > 0): #Busca si el caracter actual es un punto
                if(not punto): #Verifica que el número no tenga más de un punto
                    punto = True
                else:
                    return False
            else:
                return False
        return True
    else:
        return False

system("clear")

#ax + b = 0
#x = -b/a
numa = input("Ingresa A: ")
numb = input("Ingresa B: ")
if(validar(numa) and validar(numb)):
    numa = float(numa)
    numb = float(numb)
    if(numa != 0):
        print(f"Solución única: {-numb/numa}")
    else:
        if(numb == 0):
            print("No hay solución única.")
        else:
            print("Sin solución.")
else:
    print("Ingrese números válidos.")