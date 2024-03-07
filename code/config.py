import os
PANTALLA = (300,450)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def guardar_info(puntos):
    with open("info.txt", "w") as archivo:
        # Escribir en el archivo
        archivo.write(str(puntos))

def leer_contenido():
    # Abrir el archivo en modo lectura
    with open("info.txt", "r") as archivo:
        # Leer y devolver todo el contenido del archivo
        contenido = archivo.read()
        return contenido
    
def crear_archivo():
    if not os.path.exists("info.txt"):
        # Abrir el archivo en modo escritura condicional para crearlo solo si no existe
        with open("info.txt", "x") as archivo:
            pass  # No hacemos nada, simplemente abrimos el archivo en blanco
    else:
        print("El archivo ya existe.")
