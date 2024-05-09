import os
import platform
import psutil

# Solicitar al usuario la ubicación donde desea crear la nueva carpeta
ubicacion = input("Ingrese la ubicación donde desea crear la nueva carpeta: ")

# Crear la nueva carpeta
nombre_carpeta = "Informacion del Sistema"
ruta_carpeta = os.path.join(ubicacion, nombre_carpeta)
os.makedirs(ruta_carpeta, exist_ok=True)

print(f"Se ha creado la carpeta '{nombre_carpeta}' en {ubicacion}")

# Crear 10 archivos.txt dentro de la nueva carpeta
tipos_info = [
    "Nombre del sistema",
    "Nombre del host",
    "Versión del sistema",
    "Procesador",
    "Uso de CPU",
    "Memoria total",
    "Memoria usada",
    "Memoria libre",
    "Espacio total en disco",
    "Espacio usado en disco",
    "Espacio libre en disco"
]

for i in range(1, 11):
    nombre_archivo = f"archivo{i}.txt"
    ruta_archivo = os.path.join(ruta_carpeta, nombre_archivo)
    
    # Obtener información del sistema
    info_sistema = platform.uname()
    cpu_info = psutil.cpu_percent(interval=1)
    mem_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')
    
    # Escribir información específica en el archivo
    with open(ruta_archivo, 'w') as archivo:
        if i == 1:
            archivo.write(f"{tipos_info[i-1]}: {info_sistema.system}\n")
        elif i == 2:
            archivo.write(f"{tipos_info[i-1]}: {info_sistema.node}\n")
        elif i == 3:
            archivo.write(f"{tipos_info[i-1]}: {info_sistema.release}\n")
        elif i == 4:
            archivo.write(f"{tipos_info[i-1]}: {info_sistema.processor}\n")
        elif i == 5:
            archivo.write(f"{tipos_info[i-1]}: {cpu_info}%\n")
        elif i == 6:
            archivo.write(f"{tipos_info[i-1]}: {mem_info.total / (1024 * 1024)} MB\n")
        elif i == 7:
            archivo.write(f"{tipos_info[i-1]}: {mem_info.used / (1024 * 1024)} MB\n")
        elif i == 8:
            archivo.write(f"{tipos_info[i-1]}: {mem_info.available / (1024 * 1024)} MB\n")
        elif i == 9:
            archivo.write(f"{tipos_info[i-1]}: {disk_info.total / (1024 * 1024 * 1024)} GB\n")
        elif i == 10:
            archivo.write(f"{tipos_info[i-1]}: {disk_info.used / (1024 * 1024 * 1024)} GB\n")
        else:
            archivo.write(f"{tipos_info[i-1]}: {disk_info.free / (1024 * 1024 * 1024)} GB\n")
    
    print(f"Se ha creado el archivo '{nombre_archivo}' en {ruta_carpeta} con información del sistema.")
