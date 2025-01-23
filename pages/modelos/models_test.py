import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression  # Si estás usando scikit-learn

# Cargar el modelo
model = joblib.load('Coffee_price_model.pkl')

# Obtener el número de características de entrada
n_features = model.n_features_in_
print(f"El modelo espera {n_features} características de entrada.")

# Obtener los coeficientes del modelo
coeficientes = model.coef_
print(f"Coeficientes del modelo: {coeficientes}")

# Intercepto del modelo
intercepto = model.intercept_
print(f"Intercepto del modelo: {intercepto}")

# Cargar los datos desde el archivo CSV
data = pd.read_csv('C:/Users/catal/OneDrive/Documentos/Carpeta Sebastian/Proyecto_N/Proyecto_Nutresa/Data/materia_prima.csv', sep=';')

# Renombrar la columna 'Date' a 'ds'
data.rename(columns={'Date': 'ds'}, inplace=True)

# Convertir la columna 'ds' a datetime y cambiar el formato a YYYY-MM-DD
data['ds'] = pd.to_datetime(data['ds'], format='%d/%m/%Y')

data = data.dropna(subset=['ds'])

# Convertir las fechas a valores numéricos (timestamps)
data['ds_numeric'] = data['ds'].map(pd.Timestamp.timestamp)

columnas_a_convertir = ['cafe_nal', 'cantidad_cafe', 'Precio_cafe', 'cantidad_cacao', 'Precio_cacao_und']

# Reemplazar comas por puntos y convertir a flotante
for columna in columnas_a_convertir:
    # Verificar si la columna es de tipo objeto (string) antes de hacer la conversión
    if data[columna].dtype == 'object':
        data[columna] = data[columna].str.replace(',', '.').astype(float)

# Asegúrate de que no haya valores nulos
data = data.dropna(subset=columnas_a_convertir)

# Eliminar columnas no deseadas
foo = data.drop([ 'Precio_carne_res','cerdo_nal', 'Precio_carne_cerdo',
                  'cantid_carne_cerdo', 'res_nal', 'cant_carne_res'], axis=1)

# Rellenar valores nulos
foo = foo.ffill()

# Asumimos que 'ds_numeric' es nuestra característica (X)
X = foo[['Precio_cacao_und','cafe_nal','cantidad_cafe','Precio_cafe','cantidad_cacao']]  # Aquí usamos las fechas convertidas en numéricas

# Realizar las predicciones usando el modelo entrenado
forecast = model.predict(X)

# Mostrar las predicciones
print(f"Predicciones: {forecast}")


