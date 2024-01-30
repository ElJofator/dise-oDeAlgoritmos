# Desarrolle un programa que calcule la media armónica de una secuencia de números.

# El programa primero debe preguntar al usuario cuántos números ingresará. A continuación, pedirá al usuario que ingrese cada uno de los n
#  números reales. Finalmente, el programa mostrará el resultado.
from modules.validate import validar
cantidad = ""
while(not cantidad.isnumeric()):
    cantidad = input("¿Cuántos números?: ")
cantidad = int(cantidad)
suma = 0
for i in range(cantidad):
    numero = ""
    while(not validar(numero)):
        numero = input(f"n{i+1} = ")
    numero = float(numero)
    if(numero != 0):
        suma += 1/numero
    else:
        i -= 1
if(suma != 0):
    print(f"H = {cantidad/suma}")
else:
    print("No se pudo calcular.")