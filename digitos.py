#Escriba un programa que determine la cantidad de dígitos en un número entero ingresado por el usuario:
from os import system

system("clear")

numero = input("Ingrese un número: ")
if(numero.isnumeric()):
    print(f"El número tiene {len(numero)} dígitos")
else:
    print("No es un número válido")