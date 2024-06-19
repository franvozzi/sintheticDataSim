import pandas as pd
import numpy as np

# Configurar la semilla para reproducibilidad
np.random.seed(42)

# Generar fechas
date_range = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D')

# Listas de productos y categorías
productos = ['Producto A', 'Producto B', 'Producto C', 'Producto D']
categorias = ['Electrónica', 'Hogar', 'Ropa', 'Juguetes']
regiones = ['Norte', 'Sur', 'Este', 'Oeste']

# Crear listas para almacenar datos
fechas = []
productos_lista = []
categorias_lista = []
regiones_lista = []
precios = []
unidades_vendidas = []

# Generar datos sintéticos
for date in date_range:
    for producto in productos:
        fechas.append(date)
        productos_lista.append(producto)
        categoria = np.random.choice(categorias)
        categorias_lista.append(categoria)
        region = np.random.choice(regiones)
        regiones_lista.append(region)
        precio = np.round(np.random.uniform(10, 100), 2)
        precios.append(precio)
        unidades = np.random.poisson(lam=50)
        unidades_vendidas.append(unidades)

# Crear DataFrame
data = {
    'Fecha': fechas,
    'Producto': productos_lista,
    'Categoría': categorias_lista,
    'Región': regiones_lista,
    'Precio': precios,
    'Unidades Vendidas': unidades_vendidas
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ventas_sinteticas.csv', index=False)

print("Datos de ventas sintéticos generados y guardados en 'ventas_sinteticas.csv'.")
