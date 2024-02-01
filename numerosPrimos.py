def esPrimo(num):
    if(num >= 2):
        for i in range(2, int(num**0.5) + 1):
            if(num%i == 0):
                return False
        return True
    else:
        return False

#Escriba un programa que reciba como entrada un número natural, e indique si es primo o compuesto:
def primo():
    num = ""
    while(not num.isnumeric()):
        num = input("Ingrese un número: ")
    num = int(num)
    if(esPrimo(num)):
        print(f"{num} es primo")
    else:
        print(f"{num} es compuesto")

#Escriba un programa que muestre los n primeros números primos, donde n es ingresado por el usuario:
def numeroDePrimos():
    cantidad = ""
    while(not cantidad.isnumeric()):
        cantidad = input("¿Cuántos primos?: ")
    cantidad = int(cantidad)
    primos = 0
    num = 2
    while(primos <= cantidad):
        if(esPrimo(num)):
            print(num)
            primos += 1
        num += 1

#Escriba un programa que muestre los números primos menores que m, donde m es ingresado por el usuario:
def primosMenoresA():
    max = ""
    while(not max.isnumeric()):
        max = input("Primos menores que: ")
    max = int(max)
    for num in range(2,max):
        if(esPrimo(num)):
            print(num)

#Escriba un programa que cuente cuántos son los números primos menores que m, donde m es ingresado por el usuario:
def contarPrimosMenoresA():
    max = ""
    while(not max.isnumeric()):
        max = input("Contar primos menores que: ")
    max = int(max)
    primos = 0
    for num in range(2,max):
        if(esPrimo(num)):
            primos += 1
    print(f"Hay {primos} primos menores que {max}")

# Todos los números naturales mayores que 1 pueden ser factorizados de una única manera como un producto de divisores primos.
# Escriba un programa que muestre los factores primos de un número entero ingresado por el usuario:
def productoDivisoresPrimos():
    num = ""
    while(not num.isnumeric()):
        num = input("Ingrese un número: ")
    num = int(num)