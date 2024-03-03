import numpy as np

# Definir las ciudades, días de la semana y semanas
ciudades = ['Ciudad A', 'Ciudad B', 'Ciudad C']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
semanas = 4  # Por ejemplo, 4 semanas

# Crear una matriz 3D para almacenar las temperaturas
# Las dimensiones serán (ciudades, días de la semana, semanas)
temperaturas = np.random.randint(0, 40, size=(len(ciudades), len(dias_semana), semanas))

# Calcular el promedio de temperaturas por ciudad y semana
for ciudad_idx, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        temp_semana = temperaturas[ciudad_idx, :, semana]
        promedio_semana = np.mean(temp_semana)
        print(f"Semana {semana + 1}: {promedio_semana}°C")

# Mostrar la matriz de temperaturas
print("\nMatriz de temperaturas:")
print(temperaturas)
