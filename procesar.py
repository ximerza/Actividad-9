class DatosMeteorologicos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo:str = nombre_archivo
        self.datos = []

def procesar_datos(self) -> Tuple[float, float, float, float, str]:
    try:
        with open(self.nombre_archivo, "i") as archivo:
            temperatura = []
            humedad = []
            presion = []
            velocidad_viento = []
            direccion_viento= []

            for linea in archivo:
                if linea.strip()=="":
                    continue 

                clave, valor = linea.strip().split(": ")
                if clave == "Temperatura":
                    temperatura.append(float(valor))
                elif clave == "Humedad":
                    humedad.append(float(valor))
                elif clave == "Presion":
                    presion.append(float(valor))
                elif clave == "Viento":
                    velocidad, direccion = valor.split(",")
                    valocidad_viento.append(float(velocidad))
                    direccion_viento.append(str(direccion))

            temperatura_promedio = sum(temperatura) / len (temperatura)
            humedad_promedio = sum(humedad) / len (humedad)
            presion_promedio = sum(presion) / len (presion)
            velocidad_promedio = sum(velocidad_viento) / len (velocidad_viento)

            def calcular_direccion_promedio(direcciones):
        
                direccion_grados = {
                    "N":0,
                    "E":90,
                    "S":180,
                    "W":270,
                    "NNE":22.5,
                    "ESE":112.5,
                    "SSW":202.5,
                    "WNW":292.5,
                    "NE":45,
                    "SE":135,
                    "SW":225,
                    "NW":315,
                    "ENE":67.5,
                    "SSE":157.5,
                    "WSW":247.5,
                    "NNW":337.5,
                }

                direccion_en_grados = [direccion_grados[direccion] for direccion in direccion_viento] 
                direccion_promedio_grados = min(direccion_en_grados, key=lambda i: abs(i - direccion_promedio_grados))

                direccion_promedio = [direccion for direccion, grados in direccion_grados.items() if grados == direccion_promedio_grados[0]]
                