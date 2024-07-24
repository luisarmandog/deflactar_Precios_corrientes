#########################################################################################################################
SCRIPT PARA DEFLACTAR CIFRAS CON BASE DE DATOS DEL BANREP Y BASE 2018

# Deflactar Cifras Anuales en Colombia con Base 2018

Este repositorio contiene un script en Python para deflactar cifras anuales utilizando datos del Banco de la República de Colombia con base en el año 2018. El objetivo del script es ajustar los valores monetarios a precios constantes de 2018, permitiendo comparaciones precisas y consistentes a lo largo del tiempo.

## Descripción

El script descarga un archivo Excel con los coeficientes de deflación desde GitHub, lee datos de un archivo CSV con cifras anuales, y ajusta estas cifras a precios constantes de 2018 utilizando los coeficientes de deflación. El resultado es guardado en un nuevo archivo CSV.

### Funcionalidades principales

- Descarga de archivo Excel con coeficientes de deflación desde una URL.
- Lectura de datos de un archivo CSV local.
- Cálculo de cifras ajustadas a precios constantes utilizando los coeficientes de deflación.
- Guardado de los resultados en un nuevo archivo CSV.
- Verificación y manejo de valores NA (faltantes) en los datos.

## Requisitos

Para ejecutar el script, asegúrate de tener instaladas las siguientes bibliotecas de Python:

- `pandas`
- `openpyxl`
- `requests`

Puedes instalarlas utilizando `pip`:

```bash
pip install pandas openpyxl requests
