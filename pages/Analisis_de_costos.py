import streamlit as st
import login
import pandas as pd
import joblib
from prophet import Prophet  # Asegúrate de tener Prophet importado
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

# Lógica de inicio de sesión
login.generar_login()
if 'usuario' in st.session_state:

    # Cargar el modelo
    model = joblib.load('pages/modelos/Beef_price_model.pkl')

    # Cargar los datos desde el archivo CSV
    data = pd.read_csv('Data/materia_prima.csv', sep=';')

    # Renombrar la columna 'Date' a 'ds'
    data.rename(columns={'Date': 'ds'}, inplace=True)

    # Convertir la columna 'ds' a datetime y cambiar el formato a YYYY-MM-DD
    data['ds'] = pd.to_datetime(data['ds'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # Eliminar columnas no deseadas
    foo = data.drop(['Precio_cacao_und', 'cantidad_cacao', 'cafe_nal', 'Precio_cafe', 'cantidad_cafe',
                    'cerdo_nal', 'Precio_carne_cerdo', 'cantid_carne_cerdo', 'res_nal', 'cant_carne_res'], axis=1)

    # Rellenar valores nulos
    foo = foo.ffill()

    # Crear un DataFrame con las fechas futuras (por ejemplo, los próximos 36 meses)
    future = model.make_future_dataframe(periods=36, freq='M')

    # Realizar las predicciones
    forecast = model.predict(future)

    # Mostrar las predicciones
    st.header('Predicción de :orange[precio de la carne de res]')
    
    # Configurar el índice del DataFrame de pronóstico a 'ds'
    forecast.set_index('ds', inplace=True)

    # Mostrar gráfico de líneas de las predicciones
    st.line_chart(forecast[['yhat', 'yhat_lower', 'yhat_upper']], height=400, width=700)

    # Mostrar información del forecast
    st.write(forecast[['yhat', 'yhat_lower', 'yhat_upper']].head())
    
    # Procesar información de precios
    precios_info = pd.read_csv('Data/materia_prima.csv', sep=';')
    precios_info['Date'] = pd.to_datetime(precios_info['Date'], format='%d/%m/%Y', errors='coerce')






     # Cargar el modelo entrenado con KNeighborsRegressor
    model = joblib.load('pages/modelos/Pork_price_model.pkl')

    # Cargar los datos desde el archivo CSV
    data = pd.read_csv('Data/materia_prima.csv', sep=';')

    # Renombrar la columna 'Date' a 'ds' y convertir a datetime
    data.rename(columns={'Date': 'ds'}, inplace=True)
    data['ds'] = pd.to_datetime(data['ds'], format='%d/%m/%Y', errors='coerce')

    # Seleccionar características relevantes
    features = data.drop(['ds',  'cantidad_cacao', 'cafe_nal',
                           'Precio_cafe', 'cantidad_cafe', 'Precio_carne_res',
    'res_nal', 'cant_carne_res'], axis=1).ffill()
    


    # Reemplazar comas por puntos y convertir a float de manera segura
    features = features.apply(lambda x: pd.to_numeric(x.astype(str).str.replace(',', '.', regex=False), errors='coerce'))

    # Llenar valores faltantes después de la conversión
    features.fillna(0, inplace=True)

    # Escalar los datos
    scaler = StandardScaler()
    features_scaled = scaler.fit_transform(features)

    # Realizar predicciones
    predictions = model.predict(features_scaled)

    # Crear DataFrame de predicciones con fechas correspondientes
    prediction_df = pd.DataFrame({
        'Fecha': data['ds'],
        'Predicción Precio Carne Cerdo': predictions
    })

    # Mostrar las predicciones
    st.header('Predicción de :orange[Precio de la Carne de Cerdo]')
    st.write(prediction_df.head())

    # Mostrar gráfico de las predicciones
    st.line_chart(prediction_df.set_index('Fecha'), height=400)

        # Mostrar cuántas características espera el modelo
    st.write(f"El modelo espera {model.n_features_in_} características.")

    # Revisar las columnas usadas en el modelo
    st.write("Columnas del DataFrame después de la selección:", features.columns.tolist())

    st.write("Revisar estadísticas del dataset:")
    st.write(features.describe())

    print(features.head())


    # print(features['Precio_carne_cerdo'].unique())

    # print(features.columns)






    
    # Realizar conversiones de precios
    precios_info['Precio_cacao_un'] = precios_info['Precio_cacao_und'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_cac'] = precios_info['cantidad_cacao'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_caf'] = precios_info['Precio_cafe'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_caf'] = precios_info['cantidad_cafe'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_carne_cerd'] = precios_info['Precio_carne_cerdo'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_carne_cer'] = precios_info['cantid_carne_cerdo'].astype(str).str.replace(',', '').astype(float)
    precios_info['Precio_carne_re'] = precios_info['Precio_carne_res'].astype(str).str.replace(',', '').astype(float)
    precios_info['cantidad_carne_r'] = precios_info['cant_carne_res'].astype(str).str.replace(',', '').astype(float)

    # Calcular ingresos
    precios_info['VentasCacao'] = precios_info['Precio_cacao_un'] * precios_info['cantidad_cac']
    precios_info['VentasCafe'] = precios_info['Precio_caf'] * precios_info['cantidad_caf']
    precios_info['VentasCarneCerdo'] = precios_info['Precio_carne_cerd'] * precios_info['cantidad_carne_cer']
    precios_info['VentasCarneRes'] = precios_info['Precio_carne_re'] * precios_info['cantidad_carne_r']

    # Mostrar información de precios
    st.write(precios_info.head())
    st.write(precios_info.info())
    
    precios_info = precios_info.set_index('Date')

    # Análisis de costos a lo largo del tiempo
    st.header('Análisis de :orange[costos a lo largo del tiempo]')

    st.subheader("Precios del :orange[Cacao] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_cacao_und'], height=400, width=700)

    st.subheader("Precios del :orange[Café] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_cafe'], height=400, width=700)

    st.subheader("Precios de la :orange[Carne de cerdo] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_carne_cerdo'], height=400, width=700)

    st.subheader("Precios de la :orange[Carne de res] a lo largo del tiempo")
    st.line_chart(precios_info['Precio_carne_res'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Cacao] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCacao'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Café] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCafe'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Carne de cerdo] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCarneCerdo'], height=400, width=700)

    st.subheader("Ingresos por ventas de :orange[Carne de res] a lo largo del tiempo")
    st.line_chart(precios_info['VentasCarneRes'], height=400, width=700)


    

    




