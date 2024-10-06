# 1. Crear y escribir en el archivo
with open('my_notes.txt', 'w') as file:
    file.write('Jugar basquet.\n')
    file.write('Leer un libro nuevo cada mes.\n')
    file.write('Practicar meditación diariamente.\n')

# 2. Leer el contenido del archivo línea por línea
with open('my_notes.txt', 'r') as file:
    lines = file.readlines()

# 3. Mostrar cada línea en la consola
for line in lines:
    print(line.strip())

# 4. No es necesario cerrar el archivo manualmente, ya que 'with' se encarga de ello automáticamente.
