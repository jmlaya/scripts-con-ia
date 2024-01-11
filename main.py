import pymongo
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from bson import ObjectId

# Función para convertir ObjectId a string
def convert_objectid(val):
    if isinstance(val, ObjectId):
        return str(val)
    return val

# Función para convertir estructuras de datos complejas a string
def convert_complex_to_string(val):
    if isinstance(val, (dict, list)):
        return str(val)
    return val

# Función para analizar de manera recursiva campos anidados
def parse_nested_fields(document, prefix=''):
    fields = {}
    for key, value in document.items():
        if isinstance(value, dict):
            nested_fields = parse_nested_fields(value, prefix=prefix + key + '.')
            fields.update(nested_fields)
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            nested_fields = parse_nested_fields(value[0], prefix=prefix + key + '.')
            fields.update(nested_fields)
        else:
            value = convert_objectid(value)
            value = convert_complex_to_string(value)
            fields[prefix + key] = {'type': str(type(value).__name__), 'example': value}
    return fields

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["dummy-db"]

# Crear un archivo de Excel
wb = Workbook()
wb.remove(wb.active)  # Remover la hoja por defecto si no se va a utilizar

# Bandera para verificar si se ha añadido alguna hoja
hoja_agregada = False

for collection_name in db.list_collection_names():
    collection = db[collection_name]
    
    # Analizar los documentos para obtener la estructura de los campos
    fields = {}
    for document in collection.find().limit(100):  # Limita la cantidad para el ejemplo
        nested_fields = parse_nested_fields(document)
        for key, value in nested_fields.items():
            if key not in fields:
                fields[key] = value

    # Si no hay campos, pasa a la siguiente colección
    if not fields:
        continue

    # Crear DataFrame para la colección
    df = pd.DataFrame.from_dict(fields, orient='index').reset_index()
    df.columns = ['field', 'type', 'example']

    # Agregar hoja al archivo de Excel
    sheet = wb.create_sheet(title=collection_name)
    for r in dataframe_to_rows(df, index=False, header=True):
        sheet.append(r)
    
    hoja_agregada = True

# Verificar si se ha agregado al menos una hoja
if not hoja_agregada:
    wb.create_sheet(title="Sheet1")

# Guardar el archivo de Excel
wb.save('MongoDB_Documentation.xlsx')
