from modules.validate import esPrimo
from os import system

# Según Sheldon, el mejor número es el 73.

# 73 es el 21er número primo. Su espejo, 37, es el 12mo número primo. 21 es el producto de multiplicar 7 por 3. En binario, 73 es un palíndromo: 1001001.

# Escriba programas que le permitan responder las siguientes preguntas:

# 1. ¿Existen otros valores p que sean el n-ésimo primo, tales que espejo(p) es el espejo(n)-ésimo primo?
# 2. ¿Existen otros valores p que sean el n-ésimo primo, tales que n es el producto de los dígitos de p?
# 3. ¿Cuáles son los primeros diez números primos cuya representación binaria es un palíndromo?

def espejo():
    bandera = True
    primos = []
    num = 0
    while(bandera):
        if(esPrimo(num)):
            primos.append(num)
            #if(num != 73):
            inv_num = int(str(num)[::-1])
            if(num != inv_num):
                if(inv_num in primos):
                    cantidad = len(primos)
                    inv_cantidad = int(str(cantidad)[::-1]) 
                    if(inv_cantidad <= cantidad):
                        if(primos[inv_cantidad-1] == inv_num):
                            print(f"{num} es el {cantidad}-avo número primo. Su espejo, {inv_num}, es el {inv_cantidad}-avo número primo.")
                            opc = input("¿Deseas continuar? (Responde 'No' si quieres parar): ").lower()
                            if (opc == "no"):
                                print(f"Se encontraron {cantidad} números.")
                                return True
        num += 1

def producto_digitos():
    bandera = True
    num = 0
    cont = 0
    cantidad = 0
    while(bandera):
        if(esPrimo(num)):
            cont += 1
            producto = 1
            cadena = str(num)
            for i in range(len(cadena)):
                producto *= int(cadena[i])
            if(producto == cont):
                print(f"{num} es el {cont}-avo número primo y el producto de sus dígitos es igual a {cont}")
                cantidad += 1
                opc = input("¿Deseas continuar? (Responde 'No' si quieres parar): ").lower()
                if (opc == "no"):
                    print(f"Se encontraron {cantidad} números.")
                    return True
        num += 1

def binarios_primos_palindromos():
    num = 0
    cantidad = 0
    while(cantidad < 10):
        if(esPrimo(num)):
            binario = str(format(num,"b"))
            inverso = binario[::-1]
            if(binario == inverso):
                cantidad += 1
                print(f"{cantidad}. {num} en binario es {binario} y ese binario es un número palíndromo.")

        num += 1

system("clear")
#espejo()
#producto_digitos()
binarios_primos_palindromos()