# Definimos la matriz 3D con datos de temperatura
print("Promedios de temperaturas de 3 ciudades a lo largo de 4 semanas")
print("")
# Suponemos 3 ciudades, 7 días (de lunes a domingo) y 3 semanas
temperaturas = [
    # Puyo
    [
        [27, 26, 25, 26],  # Lunes, semana 1, semana 2 y semana 3
        [24, 22, 28, 27],  # Martes
        [27, 24, 26, 26],  # Miércoles
        [28, 25, 29, 25],  # Jueves
        [28, 26, 26, 27],  # Viernes
        [29, 27, 28, 22],  # Sábado
        [26, 24, 27, 25]  # Domingo
    ],
    # Mompiche
    [
        [25, 26, 25, 26],  # Lunes
        [24, 25, 27, 24],  # Martes
        [26, 27, 24, 28],  # Miércoles
        [27, 26, 26, 26],  # Jueves
        [23, 24, 28, 26],  # Viernes
        [25, 24, 26, 25],  # Sábado
        [26, 25, 28, 25]  # Domingo
    ],
    # Cuenca
    [
        [15, 10, 10, 21],  # Lunes
        [13, 11, 11, 20],  # Martes
        [11, 11, 18, 18],  # Miércoles
        [11, 17, 22, 17],  # Jueves
        [18, 21, 21, 18],  # Viernes
        [20, 20, 15, 11],  # Sábado
        [20, 15, 21, 15]  # Domingo
    ]
]

# Ciudades y semanas
ciudades = ["Puyo", "Mompiche", "Cuenca"]
semanas = ["Semana 1", "Semana 2", "Semana 3", "Semana 4"]

# Cálculo del promedio
for ciudad in range(len(temperaturas)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]} es:")

    for semana in range(len(semanas)):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[ciudad])):
            suma_temperaturas += temperaturas[ciudad][dia][semana]

        promedio = suma_temperaturas / len(temperaturas[ciudad])
        print(f"  {semanas[semana]}: {promedio:.2f}°C")