import json
import argparse

# Función para cargar datos JSON desde un archivo
def cargar_json_desde_archivo(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        return json.load(archivo)

# Función para crear un archivo Markdown a partir de los datos JSON
def crear_markdown_desde_json(json_data, ruta_salida):
    contenido_markdown = ""

    for key, entry in json_data['mapping'].items():
        # Comprobar si la entrada tiene la clave 'message', 'parts' y el estado deseado
        if 'message' in entry and 'parts' in entry['message'].get('content', {}):
            mensaje_status = entry['message'].get('status')
            if mensaje_status in ['finished_successfully', 'finished_partial_completion']:
                # Extrayendo el rol del autor
                autor_rol = entry['message']['author']['role']

                # Extrayendo las partes del contenido del mensaje
                partes_mensaje = entry['message']['content']['parts']

                # Formateando el autor y añadiendo las partes del mensaje
                if autor_rol == 'user':
                    # Alineación a la derecha para el autor 'user'
                    contenido_markdown += f"<div align='right'><h2>{autor_rol}</h2></div>\n\n"
                else:
                    # Uso de encabezado para destacar otros autores
                    contenido_markdown += f"## {autor_rol}\n\n"

                for parte in partes_mensaje:
                    contenido_markdown += f"{parte}\n\n"

                # Añadiendo un separador después de cada mensaje
                contenido_markdown += "---\n\n"

    # Escribiendo el contenido markdown en un archivo
    with open(ruta_salida, 'w') as archivo:
        archivo.write(contenido_markdown)

# Configuración del analizador de argumentos
parser = argparse.ArgumentParser(description='Procesar y convertir conversaciones de JSON a Markdown.')
parser.add_argument('-i', '--input', default='./conversacion.json', help='Ruta al archivo JSON de entrada (default: ./conversacion.json)')
parser.add_argument('-o', '--output', default='./conversacion.md', help='Ruta al archivo Markdown de salida (default: ./conversacion.md)')

# Parseo de argumentos
args = parser.parse_args()

# Cargar los datos JSON
data_json = cargar_json_desde_archivo(args.input)

# Crear el archivo Markdown
crear_markdown_desde_json(data_json, args.output)
