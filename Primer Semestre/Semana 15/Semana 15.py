# Creamos un perfil con informacion personal ficticia
informacion_personal = {
    "nombre": "Danilo Rosero",
    "edad": 20,
    "ciudad": "Ambato",
    "profesion": "Dj"
}

# Modificamos la clave ciudad
informacion_personal["ciudad"] = "Esmeraldas"

# Agregamos una nueva clave para profesion
informacion_personal["profesion"] = "Doctor"

# Verificamos si la clave telefono existe en el perfil
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"

# Eliminamos la clave edad
if "edad" in informacion_personal:
    del informacion_personal["edad"]

# Imprimos el perfil final usando un bucle for
print("Perfil final:")
print("")
for clave, valor in informacion_personal.items():
    print(f"{clave}: {valor}")