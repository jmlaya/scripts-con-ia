# MongoDB Collections Scan

## Descripción
Con este script generado por [ChatGPT](https://chat.openai.com/share/83791335-0077-44c9-a0dd-80ce3913d2cc) generas un archivo de excel (xlsx) que tendrá el listado de colecciones de una base de datos en mongo.

## Características
- Conexión a cualquier base de datos MongoDB especificada.
- Generación de una hoja de cálculo con las colecciones de la base de datos.
- Formato estilizado en Excel para mejorar la legibilidad.

## Requisitos
Para ejecutar este script, necesitarás:
- Python 3.x
- Bibliotecas de Python: pymongo, pandas, openpyxl

## Uso
Para utilizar este script, sigue estos pasos:

1. Instalación de Dependencias:
   Asegúrate de tener instaladas las bibliotecas necesarias con el comando 
   ```bash
   pip install -r requirements.txt
   ```
2. Ejecución del Script:
   Ejecuta el script desde la línea de comandos, proporcionando el nombre de la base de datos y, opcionalmente, el string de conexión y el nombre del archivo de salida.

   Ejemplo de uso básico:
   ```bash
   python script.py -u <mongo_url> -n <database_name> -a <filepath>
   ```

   donde:
   - database_name es el nombre de tu base de datos en MongoDB.
   - mongo_url es tu string de conexión a MongoDB. El valor predeterminado es mongodb://localhost:27017.
   - filepath es el nombre deseado para el archivo de salida. El valor predeterminado es listado_de_colecciones.xlsx.

## Notas Adicionales
- Asegúrate de que MongoDB esté accesible en la dirección especificada por el string de conexión.
- Puedes modificar el script para adaptarlo a necesidades específicas, como cambiar el formato del archivo Excel o ajustar la cantidad de datos analizados por colección.
