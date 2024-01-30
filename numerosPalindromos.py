# Un número natural es un palíndromo si se lee igual de izquierda a derecha y de derecha a izquierda.

# Por ejemplo, 14941 es un palíndromo, mientras que 81924 no lo es.

# Escriba un programa que indique si el número ingresado es o no palíndromo:
num = ""
while(not num.isnumeric()):
    num = input("Ingrese un número: ")
inverso = num[::-1]
if(num == inverso):
    print(f"{num} es un número palíndromo")
else:
    print(f"{num} no es un número palíndromo")