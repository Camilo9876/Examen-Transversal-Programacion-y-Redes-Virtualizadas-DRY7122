import requests

def obtener_distancia_y_duracion(ciudad_origen, ciudad_destino):
    url_base = "https://www.mapquestapi.com/directions/v2/route"
    token = "JjPLgkMn58yOSGfL1quz1egjq5C57zty"

    parametros = {
        "key": token,
        "from": ciudad_origen,
        "to": ciudad_destino,
        "unit": "k",
        "narrativeType": "none"
    }

    respuesta = requests.get(url_base, params=parametros)
    datos = respuesta.json()

    distancia = datos["route"]["distance"]
    duracion_segundos = datos["route"]["time"]

    return distancia, duracion_segundos

def calcular_combustible(distancia):
    rendimiento_litros_km = 0.12
    combustible_requerido = distancia * rendimiento_litros_km
    return combustible_requerido

def convertir_segundos_a_horas_minutos_segundos(segundos):
    horas = segundos // 3600
    minutos = (segundos % 3600) // 60
    segundos = segundos % 60
    return horas, minutos, segundos

def imprimir_narrativa_viaje(ciudad_origen, ciudad_destino, distancia, duracion_horas, duracion_minutos, duracion_segundos, combustible_requerido):
    print ("datos del viaje:")
    print (f"Origen: {ciudad_origen}")
    print (f"Destino: {ciudad_destino}")
    print (f"Distancia: {distancia:.1f} km")
    print (f"Duración: {duracion_horas} horas, {duracion_minutos} minutos, {duracion_segundos} segundos")
    print (f"Combustible requerido: {combustible_requerido:.1f} litros")

# Solicitar ciudades de origen y destino al usuario
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")


# Obtener distancia y duración del viaje
distancia, duracion_segundos = obtener_distancia_y_duracion(ciudad_origen, ciudad_destino)

# Calcular combustible requerido
combustible_requerido = calcular_combustible(distancia)

# Convertir duración a horas, minutos y segundos
duracion_horas, duracion_minutos, duracion_segundos = convertir_segundos_a_horas_minutos_segundos(duracion_segundos)

# Imprimir narrativa del viaje

imprimir_narrativa_viaje(ciudad_origen, ciudad_destino, distancia, duracion_horas, duracion_minutos, duracion_segundos, combustible_requerido)
print ("")
print ("*******************************************************************************************************************")
print ("narrativa:")
print ("Su viaje desde la ciudad de " + str(ciudad_origen) + " hasta la ciudad de " + str(ciudad_destino) + " tiene una duración de: " + str(duracion_horas) + " horas, " + str(duracion_minutos) + " minutos y " + str(duracion_segundos) + " segundos")
print ("La distancia de su viaje tiene un alcance de " + str(distancia) + " Kilometros.")
print ("Finalmente la gasolina que utilizará en total para su viaje es de " + f"{combustible_requerido:.1f}" +  " Litros.")
print ("*******************************************************************************************************************")
print ("")

while True:
	opcion = input("Presione 's' para salir: ")
	if opcion.lower() == 's':
	    break
