# Programa 2: Ordenación de Arreglo Multidimensional
# Crear una matriz bidimensional (3x3)

matriz = [
    [3, 7, 1],
    [5, 2, 8],
    [4, 9, 6]
]

# Función para ordenar una fila de manera ascendente utilizando Bubble Sort

def bubble_sort_fila_ascendente(fila):
    n = len(fila)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]

# Función para mostrar la matriz

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

# Mostrar la matriz original

print("Matriz Original:")
mostrar_matriz(matriz)

# Ordenar cada fila de la matriz utilizando Bubble Sort

for fila in matriz:
    bubble_sort_fila_ascendente(fila)

# Mostrar la matriz ordenada

print("\nMatriz Ordenada por Filas de Manera Ascendente:")
mostrar_matriz(matriz)