from procesar.py import DatosMeteorologicos

datos = DatosMeteorologicos("datos.txt")
promedio = datos.procesar_datos()
print("Temperatura promedio:", promedio[0])
print("Humedad promedio:", promedio[1])
print("Presion promedio:", promedio[2])
print("velocidad promedio:", promedio[3])
print("Direccion del viento promedio:", promedio[4])
