#Escriba un programa que reciba como entrada las coordenadas en que se encuentra un caballo, y entregue como salida todas las casillas hacia las cuales el caballo puede desplazarse.

# Todas las coordenadas mostradas deben estar dentro del tablero.

# Si la coordenada ingresada por el usuario es inválida, el programa debe indicarlo.
print("Ingrese las coordenadas del caballo.")
fila = ""
while(not fila.isnumeric()):
    fila = input("Fila: ")
columna = ""
while(not columna.isnumeric()):
 columna = input("Columna: ")
fila = int(fila)
columna = int(columna)
if(1 <= fila <= 8 and 1 <= columna <= 8):
   mov = [[-2,-1],
          [-2,1],
          [-1,-2],
          [-1,2],
          [1,-2],
          [1,2],
          [2,-1],
          [2,1]]
   print("El caballo puede saltar a:")
   for i in range(len(mov)):
      newFila = fila + mov[i][0]
      newColumna = columna + mov[i][1]
      if(1 <= newFila <= 8 and 1 <= newColumna <= 8):
         print(f"{newFila} {newColumna}")
else:
   print("Posición inválida.")