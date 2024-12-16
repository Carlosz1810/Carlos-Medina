# 1. Crear y escribir en el archivo
with open('my_notes.txt', 'w') as file:
    file.write('Amo viajar en moto.\n')
    file.write('Me gusta muchísimo el motocross.\n')
    file.write('Amo las películas con mi novia.\n')
    file.write('Me agrada salir a conocer pueblos en moto.\n')

# 2. Leemos el contenido línea por línea
with open('my_notes.txt', 'r') as file:
    lines = file.readlines()

# 3. Mostramos cada línea
for line in lines:
    print(line.strip())

# 4. No es necesario cerrar el archivo manualmente, ya que 'with' se encarga de ello automáticamente.