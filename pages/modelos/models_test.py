import joblib
import pandas as pd
from prophet import Prophet  # Asegúrate de tener Prophet importado

# Cargar el modelo
model = joblib.load('Beef_price_model.pkl')

# Cargar los datos desde el archivo CSV
data = pd.read_csv('materia_prima.csv', sep=';')

# Renombrar la columna 'Date' a 'ds'
data.rename(columns={'Date': 'ds'}, inplace=True)

# Convertir la columna 'ds' a datetime y cambiar el formato a YYYY-MM-DD
data['ds'] = pd.to_datetime(data['ds'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

# Eliminar columnas no deseadas
foo = data.drop(['Precio_cacao_und', 'cantidad_cacao', 'cafe_nal', 'Precio_cafe', 'cantidad_cafe',
                 'cerdo_nal', 'Precio_carne_cerdo', 'cantid_carne_cerdo', 'res_nal', 'cant_carne_res'], axis=1)

# Convertir columnas de tipo 'object' a 'float' si es necesario
# for column in foo.columns:
#     if foo[column].dtype == 'object':
#         foo[column] = foo[column].str.replace(',', '.').astype(float)

# Rellenar valores nulos
foo = foo.ffill()

# Crear un DataFrame con las fechas futuras (por ejemplo, los próximos 12 meses)
future = model.make_future_dataframe(periods=36, freq='M')  # Cambia 'M' por 'D' si quieres diario

# Asegúrate de que la columna 'y' esté presente para realizar la predicción
# Si tu modelo requiere valores de 'y', puedes unir foo y future
# Pero como es un pronóstico, probablemente solo necesites future con 'ds'

# Realizar las predicciones
forecast = model.predict(future)

# Mostrar las predicciones
print(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])


