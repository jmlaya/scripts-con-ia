# Documentación del Script de Conversación JSON a Markdown

## Propósito

Este script está diseñado para procesar archivos JSON que contienen datos de conversación y convertirlos en un formato legible y bien estructurado en Markdown. Es útil para visualizar conversaciones almacenadas en formato JSON, como registros de chat o interacciones de diálogo.

## Cómo Funciona

El script analiza un archivo JSON de entrada, buscando mensajes dentro de la estructura de datos. Filtra los mensajes según su estado, incluyendo solo aquellos con estado `"finished_successfully"` o `"finished_partial_completion"`. Cada mensaje es formateado en Markdown, destacando el autor del mensaje y utilizando un separador para diferenciar entre mensajes consecutivos. 

El script ofrece flexibilidad en términos de archivos de entrada y salida, permitiendo al usuario especificar rutas personalizadas para estos archivos. Si no se especifican rutas, se utilizan valores predeterminados.

### Detalles Técnicos

- **Filtrado de Mensajes**: Solo se incluyen mensajes con estados específicos.
- **Formato del Autor**: El autor de cada mensaje se destaca con un encabezado y se alinea a la derecha para el autor "user".
- **Separadores de Mensajes**: Se utiliza un separador para diferenciar claramente entre mensajes individuales en la salida de Markdown.

## Cómo Usar

### Prerrequisitos

Asegúrate de tener Python instalado en tu sistema. Este script ha sido escrito en Python y requiere un intérprete de Python para ejecutarse.

### Ejecución del Script

1. **Especificar Archivo de Entrada (Opcional)**: 
   - Por defecto, el script busca un archivo llamado `./conversacion.json`.
   - Puedes especificar un archivo de entrada diferente usando la opción `-i` o `--input`.
   
   Ejemplo: `python gpt-parser.py -i ./miArchivoDeEntrada.json`

2. **Especificar Archivo de Salida (Opcional)**: 
   - Por defecto, el script generará un archivo llamado `./conversacion.md`.
   - Puedes especificar un archivo de salida diferente usando la opción `-o` o `--output`.
   
   Ejemplo: `python gpt-parser.py -o ./miArchivoDeSalida.md`

3. **Ejecutar el Script**:
   - Ejecuta el script en la línea de comandos, especificando las rutas de los archivos según sea necesario.
   - Si no especificas rutas, se usarán los valores predeterminados.

### Ejemplos de Comandos

- Usar archivos predeterminados: `python gpt-parser.py`
- Especificar solo archivo de entrada: `python gpt-parser.py -i ./miEntrada.json`
- Especificar ambos, archivo de entrada y salida: `python gpt-parser.py -i ./miEntrada.json -o ./miSalida.md`
