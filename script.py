###################################SCRIPT PARA DEFLACTAR CIFRAS ANUALES EN COLOMBIA CON BASE 2018 ####################################\n",
#Autor: Luis Armando Gelvez\n",
#Version 1\n",
#Actualización 23 de julio de 2024\n

# IMportamos datos
#Datos de Banrep, LINK https://totoro.banrep.gov.co/analytics/saw.dll?Download&Format=excel2007&Extension=.xls&BypassCache=true&lang=es&path=%2Fshared%2FSeries%20Estad%C3%ADsticas_T%2F1.%20IPC%20base%202018%2F1.2.%20Por%20a%C3%B1o%2F1.2.3.IPC_Por%20grupo%20de%20gasto_IQY"

# Instalar pandas y openpyxl desde el entorno de Jupyter Notebook
#%pip install pandas
#%pip install openpyxl
#%pip install requests
 # Importar las bibliotecas necesarias
import os
import pandas as pd
import requests


# Paso 1: Verifica el directorio de trabajo actual y lista los archivos
print(os.getcwd())  # Muestra el directorio de trabajo actual
print(os.listdir())  # Lista los archivos en el directorio de trabajo

# Paso 1: Descargar el archivo Excel desde GitHub
url = "https://github.com/luisarmandog/deflactar_Precios_corrientes/raw/main/ipc_BASE_2018.xlsx"
file_path = "ipc_BASE_2018.xlsx"

response = requests.get(url)
with open(file_path, 'wb') as file:
    file.write(response.content)

# Paso 2: Obtener las hojas disponibles
xls = pd.ExcelFile(file_path)
sheet_names = xls.sheet_names


# Mostrar las hojas disponibles
print("Hojas disponibles en el archivo Excel:", sheet_names)

# Paso 3: Leer el archivo CSV
file_csv = "C:/Users/LUIS/Documents/CARTOGRAFÍA ARROYOS/MODELO DE PRECIOS HEDONICO CON PESOS PONDERADOS/df_MODELO_19_ok.csv"
datos = pd.read_csv(file_csv)


# Supongamos que la hoja donde está la serie de datos se llama "COEF_ipc_BASE_2018"
sheet_name = "COEF_ipc_BASE_2018"

# Cargar la hoja específica en un DataFrame
deflactor = pd.read_excel(file_path, sheet_name=sheet_name)
# Mostrar las primeras filas del DataFrame
print("Primeras filas del DataFrame 'deflactor':")
print(deflactor.head())


# Paso 3: Leer el archivo CSV
file_csv = "C:/Users/LUIS/Documents/CARTOGRAFÍA ARROYOS/MODELO DE PRECIOS HEDONICO CON PESOS PONDERADOS/df_MODELO_19_ok.csv"
datos = pd.read_csv(file_csv)
# Mostrar un resumen del DataFramecd 
print("Información del DataFrame 'datos':")
print(datos.info())

# Paso 4: Definir la función para deflactar valores
def deflactar_valores(datos, deflactor):
    # Asegúrate de que ambas tablas tengan columnas con los nombres correctos
    # `datos` debe tener las columnas: "moda_venta" y "año_inicio_venta"
    # `deflactor` debe tener las columnas: "AÑO" y "DEFLA_COEF"
    
    # Realiza una unión entre los DataFrames por el año
    datos = datos.merge(deflactor, left_on="fecha_inicio_venta", right_on="AÑO", how="left")
    
    # Calcula los valores deflactados
    datos['PRECIOmc_MODA_DEFLAC'] = datos['preciomc_moda'] * datos['DEFLA_COEF']
    
    # Devuelve el DataFrame con la nueva columna
    return datos

# Supongamos que `datos` es tu DataFrame principal y `deflactor` es el DataFrame con los coeficientes de deflactor
# Llamamos a la función y guardamos el resultado en un nuevo DataFrame
datos_deflactados = deflactar_valores(datos, deflactor)

# Mostrar las primeras filas del DataFrame resultante
print("Primeras filas del DataFrame 'datos_deflactados':")
print(datos_deflactados.head())


# Verificar si la columna `PRECIOmc_MODA_DEFLAC` tiene datos NA
na_count = datos_deflactados['PRECIOmc_MODA_DEFLAC'].isna().sum()
print(f"Número de valores NA en PRECIOmc_MODA_DEFLAC: {na_count}")

# Mostrar las filas que contienen NA en la columna `PRECIOmc_MODA_DEFLAC`
na_rows = datos_deflactados[datos_deflactados['PRECIOmc_MODA_DEFLAC'].isna()]
print("Filas con valores NA en PRECIOmc_MODA_DEFLAC:")
print(na_rows)

# Exportar el DataFrame resultante a un archivo CSV
datos_deflactados.to_csv("deflac_df_MODELO_19_ok.csv", index=False)

