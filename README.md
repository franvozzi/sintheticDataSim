# sintheticDataSimulation, Análisis de Ventas y Predicción con Prophet

Este proyecto realiza un análisis exploratorio de datos (EDA) y predicciones de ventas utilizando la biblioteca `Prophet` de Facebook. Los datos utilizados son sintéticos y representan ventas en diferentes categorías y regiones.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

- `ventas_sinteticas.csv`: Archivo CSV con los datos de ventas.
- `notebook.ipynb`: Notebook Jupyter con el código de análisis y predicción.
- `salesData.py`: Archivo Python que genera un CSV con datos sintéticos.
- `README.md`: Este archivo.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python y las siguientes bibliotecas:

- pandas
- seaborn
- matplotlib
- prophet
- jupyter

Puedes instalarlas utilizando pip:

```bash
pip install pandas seaborn matplotlib prophet jupyter
```

## Instrucciones
1. Clonar el repositorio:
```bash
pip install pandas seaborn matplotlib prophet jupyter
```
```bash
git clone (https://github.com/franvozzi/sintheticDataSim)
cd sintheticDataSim
```
2.Instalar las dependencias:
```bash
pip install -r requirements.txt
```
3.Ejecutar el notebook Jupyter:
```bash
jupyter notebook notebook.ipynb
```

## Contenido del Notebook
### 1. Cargar y Visualizar el Archivo CSV
Cargamos los datos de ventas desde un archivo CSV y mostramos las primeras filas para verificar que los datos se hayan cargado correctamente.

### 2. Limpieza de Datos
Convertimos la columna Fecha al tipo datetime y eliminamos filas duplicadas para asegurar que nuestros datos sean únicos y precisos.

### 3. Análisis Exploratorio de Datos (EDA)
Generamos estadísticas descriptivas y visualizamos las tendencias de ventas a lo largo del tiempo, así como su distribución por categoría y región.

Tendencias de Ventas a lo Largo del Tiempo

Distribución de Ventas por Categoría

Distribución de Ventas por Región

### 4. Crear el Modelo de Predicción con Prophet
Utilizamos Prophet para crear un modelo de predicción y predecir las ventas futuras. Visualizamos las predicciones junto con la tendencia de las ventas pasadas.


## Notas
Asegúrate de actualizar la ruta del archivo CSV en el notebook si es necesario.
Los datos utilizados son sintéticos y pueden no reflejar un caso real.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue los pasos estándar para hacer un fork del repositorio, hacer tus cambios y enviar un pull request.
