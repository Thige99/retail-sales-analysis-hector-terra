import numpy as np
 

def cargar_datos(ruta_archivo):
    datos = np.genfromtxt(ruta_archivo, delimiter=',', skip_header=1, dtype=None,)
    return datos


def analisis_basico(datos):
    print(f'Dimensiones: {datos.ndim}, {datos.shape}')
    print('Primeros 5 registros:')
    print(datos[:5])

    edades = datos['f4'].astype(float)
    cantidad = datos['f6'].astype(float)
    precios = datos['f7'].astype(float)
    total = datos['f8'].astype(float)

    print(f'Media de edad: {np.mean(edades):.2f}')
    print(f'Media de cantidad: {np.mean(cantidad):.2f}')
    print(f'Media de precios: {np.mean(precios):.2f}')
    print(f'Total promedio: {np.mean(total):.2f}')


if __name__ == "__main__":
    ruta_archivo = './data/retail_sales_dataset.csv'
    datos = cargar_datos(ruta_archivo)
    analisis_basico(datos)