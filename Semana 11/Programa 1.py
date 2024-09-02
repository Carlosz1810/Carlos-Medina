# Programa 1: Búsqueda en Arreglo Multidimensional
# Crear una matriz bidimensional (3x3)

matriz = [
    [4, 8, 3],
    [7, 2, 6],
    [1, 5, 9]
]

# Búsqueda de un valor en la matriz

valor_buscado = int(input("Valor a buscar en la matriz: "))
if any(valor_buscado in fila for fila in matriz):
    print(f"El valor {valor_buscado} si se encuentra en la matriz.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")

# Inicializar variables para buscar la ubicacion del valor

fila_encontrada = -1
columna_encontrada = -1

# Recorrer la matriz para buscar el valor

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        if matriz[fila][columna] == valor_buscado:
            fila_encontrada = fila
            columna_encontrada = columna
            break
    if fila_encontrada != -1:
        break

# Mostrar que si se encontró el valor y en cual la posición en la que está ubicado

if fila_encontrada != -1:
    print(f"{valor_buscado} Se encuentra ubicado en la fila {fila_encontrada} y en la columna {columna_encontrada}.")
else:
    print(f"{valor_buscado} no se encontró en la matriz.")