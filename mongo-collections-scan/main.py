import argparse
import pymongo
import pandas as pd

def obtener_colecciones(url, nombre_base_datos):
    # Conectarse a MongoDB
    client = pymongo.MongoClient(url)
    
    # Seleccionar la base de datos
    db = client[nombre_base_datos]
    
    # Obtener el listado de colecciones
    colecciones = db.list_collection_names()
    
    return colecciones

def guardar_en_excel(colecciones, archivo):
    # Crear un DataFrame de pandas con las colecciones
    df = pd.DataFrame(colecciones, columns=["Colecciones"])
    
    # Guardar el DataFrame en un archivo Excel
    df.to_excel(archivo, index=False)

def main():
    # Configurar el argumento de línea de comandos
    parser = argparse.ArgumentParser(description="Obtener el listado de colecciones en una base de datos MongoDB y guardarlas en un archivo Excel.")
    parser.add_argument("--url", "-u", type=str, default="mongodb://localhost:27017/", help="URL de la base de datos MongoDB (por defecto: mongodb://localhost:27017/)")
    parser.add_argument("--nombre_base_datos", "-n", type=str, default="nombre_de_tu_base_de_datos", help="Nombre de la base de datos MongoDB (por defecto: nombre_de_tu_base_de_datos)")
    parser.add_argument("--archivo", "-a", type=str, default="listado_de_colecciones.xlsx", help="Ruta y nombre del archivo XLSX de salida (por defecto: listado_de_colecciones.xlsx)")
    args = parser.parse_args()
    
    # Obtener el listado de colecciones
    colecciones = obtener_colecciones(args.url, args.nombre_base_datos)
    
    # Guardar el listado de colecciones en un archivo Excel
    guardar_en_excel(colecciones, args.archivo)

if __name__ == "__main__":
    main()
