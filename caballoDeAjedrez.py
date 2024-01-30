print("Ingrese las coordenadas del caballo.")
fila = ""
while(not fila.isnumeric()):
    fila = input("Fila: ")
columna = ""
while(not columna.isnumeric()):
 columna = input("Columna: ")
fila = int(fila)
columna = int(columna)