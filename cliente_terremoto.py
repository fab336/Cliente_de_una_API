import requests

def get_earthquake_data(min_magnitude):
    # URL para solicitar eventos sísmicos
    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson",  # Formato de respuesta
        "starttime": "2023-01-01",  # Fecha de inicio
        "endtime": "2023-12-31",    # Fecha de fin
        "minmagnitude": min_magnitude  # Magnitud mínima definida por el usuario
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()  # Respuesta en formato JSON
        if not data["features"]:  # Verifica si no hay resultados
            print("No se ha encontrado ningún terremoto con la magnitud especificada.")
            return []
        return data["features"]  # Lista de terremotos
    else:
        print("Error al obtener datos:", response.status_code)
        return []

# Bucle para repetir la consulta
while True:
    # Solicita al usuario el número de terremotos y la magnitud mínima
    try:
        num_earthquakes = int(input("Número de terremotos a mostrar: "))
        min_magnitude = float(input("Magnitud mínima del terremoto: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    # Ejecución del cliente con parámetros del usuario
    earthquakes = get_earthquake_data(min_magnitude)

    # Verifica si hay resultados antes de imprimir
    if earthquakes:
        # Mostrar los primeros terremotos según la cantidad especificada por el usuario
        for earthquake in earthquakes[:num_earthquakes]:  
            properties = earthquake["properties"]
            print(f"Lugar: {properties['place']}")
            print(f"Magnitud: {properties['mag']}")
            print(f"Fecha y hora: {properties['time']}\n")

    # Preguntar si el usuario quiere realizar otra consulta
    again = input("¿Quieres hacer otra consulta? (s/n): ").strip().lower()
    if again != 's':
        print("Programa finalizado.")
        break
