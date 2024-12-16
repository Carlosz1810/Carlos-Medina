# Definimos la matriz 3D con datos de temperatura
# Suponemos 3 ciudades, 7 días (de lunes a domingo) y 3 semanas
temperaturas = [
    # Puyo
    [
        [27, 26, 25],  # Lunes, semana 1, semana 2 y semana 3
        [24, 22, 28],  # Martes
        [27, 24, 26],  # Miércoles
        [28, 25, 29],  # Jueves
        [28, 26, 26],  # Viernes
        [29, 27, 28],  # Sábado
        [26, 24, 27]  # Domingo
    ],
    # Mompiche
    [
        [25, 26, 25],  # Lunes
        [24, 25, 27],  # Martes
        [26, 27, 24],  # Miércoles
        [27, 26, 26],  # Jueves
        [23, 24, 28],  # Viernes
        [25, 24, 26],  # Sábado
        [26, 25, 28]  # Domingo
    ],
    # Cuenca
    [
        [15, 10, 10],  # Lunes
        [13, 11, 11],  # Martes
        [11, 11, 18],  # Miércoles
        [11, 17, 22],  # Jueves
        [18, 21, 21],  # Viernes
        [20, 20, 15],  # Sábado
        [20, 15, 21]  # Domingo
    ]
]

# Ciudades y semanas
ciudades = ["Puyo", "Mompiche", "Cuenca"]
semanas = ["Semana 1", "Semana 2", "Semana 3"]

# Cálculo del promedio
for ciudad in range(len(temperaturas)):
    print(f"Promedio de temperaturas para {ciudades[ciudad]} es:")

    for semana in range(len(semanas)):
        suma_temperaturas = 0
        for dia in range(len(temperaturas[ciudad])):
            suma_temperaturas += temperaturas[ciudad][dia][semana]

        promedio = suma_temperaturas / len(temperaturas[ciudad])
        print(f"  {semanas[semana]}: {promedio:.2f}°C")