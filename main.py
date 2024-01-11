import pymongo
import pandas as pd
from openpyxl import Workbook
from openpyxl.utils.dataframe import dataframe_to_rows
from bson import ObjectId, Timestamp

# Mapeo de tipos de Python a tipos de MongoDB
tipo_mongo = {
    'str': 'String',
    'int': 'Int32',
    'float': 'Double',
    'bool': 'Boolean',
    'ObjectId': 'ObjectId',
    'datetime': 'Date',
    'Timestamp': 'Timestamp',  # Agregado para manejar Timestamp de BSON
    # Añade más mapeos según sea necesario
}

# Función para obtener el tipo de MongoDB
def get_mongo_type(val):
    if isinstance(val, ObjectId):
        return 'ObjectId'
    elif isinstance(val, Timestamp):
        return 'Timestamp'
    else:
        python_type = type(val).__name__
        return tipo_mongo.get(python_type, python_type)

# Función para analizar de manera recursiva campos anidados
def parse_nested_fields(document, prefix=''):
    fields = {}
    for key, value in document.items():
        value_type = get_mongo_type(value)

        if isinstance(value, (ObjectId, Timestamp)):
            value_example = str(value)
        elif isinstance(value, (dict, list)):
            value_example = str(value)
            value_type = 'String'
        else:
            value_example = value

        if isinstance(value, dict):
            nested_fields = parse_nested_fields(value, prefix=prefix + key + '.')
            fields.update(nested_fields)
        elif isinstance(value, list) and value and isinstance(value[0], dict):
            nested_fields = parse_nested_fields(value[0], prefix=prefix + key + '.')
            fields.update(nested_fields)
        else:
            fields[prefix + key] = {'type': value_type, 'example': value_example}
    return fields

# Conexión a MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
db = client["dummy-db"]

# Crear un archivo de Excel
wb = Workbook()
wb.remove(wb.active)  # Remover la hoja por defecto si no se va a utilizar

# Ordenar las colecciones alfabéticamente
collection_names = sorted(db.list_collection_names())

for collection_name in collection_names:
    collection = db[collection_name]
    
    # Analizar los documentos para obtener la estructura de los campos
    fields = {}
    for document in collection.find().limit(100):
        nested_fields = parse_nested_fields(document)
        for key, value in nested_fields.items():
            if key not in fields:
                fields[key] = value

    # Ordenar los campos alfabéticamente antes de crear el DataFrame
    sorted_fields = dict(sorted(fields.items()))

    # Si no hay campos, pasa a la siguiente colección
    if not sorted_fields:
        continue

    # Crear DataFrame para la colección
    df = pd.DataFrame.from_dict(sorted_fields, orient='index').reset_index()
    df.columns = ['field', 'type', 'example']

    # Agregar hoja al archivo de Excel
    sheet = wb.create_sheet(title=collection_name)
    for r in dataframe_to_rows(df, index=False, header=True):
        sheet.append(r)

# Guardar el archivo de Excel
wb.save('MongoDB_Documentation.xlsx')
