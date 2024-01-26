# Desarrolle un programa que calcule el dígito verificador de un rol UTFSM.

# Para calcular el dígito verificador, se deben realizar los siguiente pasos:

# Obtener el rol sin guión ni dígito verificador.
# Invertir el número. (e.g: de 201012341 a 143210102).
# Multiplicar los dígitos por la secuencia 2, 3, 4, 5, 6, 7, si es que se acaban los números, se debe comenzar denuevo, por ejemplo, con 143210102:
# 1×2+4×3+3×4+2×5+1×6+0×7+1×2+0×3+2×4=52
# Al resultado obtenido, es decir, 52, debemos sacarle el módulo 11, es decir:

# 52 % 11 = 8

# Con el resultado obtenido en el paso anterior, debemos restarlo de 11:

# 11 − 8 = 3

# Finalmente, el dígito verificador será el obtenido en la resta: 201012341-3.
from os import system

system("clear")

numero = input("Ingrese un número: ")
if(numero.isnumeric()):
    invertido = numero[::-1]
    secuencia = [2,3,4,5,6,7]
    cont = 0
    suma = 0
    for i in range(len(invertido)):
        suma += int(invertido[i])*secuencia[cont]
        if(cont < len(secuencia) - 1):
            cont += 1
        else:
            cont = 0
    residuo = suma % 11
    digito = int(numero)+residuo-11
    print(f"El dígito verificador es: {digito}")
else:
    print("No es un número válido")