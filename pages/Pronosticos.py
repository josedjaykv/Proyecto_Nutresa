import streamlit as st
import pandas as pd
import login
import os
import sqlite3
import joblib
import csv
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

login.generar_login()

if 'usuario' in st.session_state:

    UPLOAD_FOLDER = 'Data'

    def get_delimiter(file_path, bytes = 4096):
        with open(file_path, 'r') as csv_file:
            data = csv_file.read(bytes) # Lee 4096 bytes del archivo
            delimiter = csv.Sniffer().sniff(data).delimiter 
            return delimiter
    st.title(':orange[Pronosticos]')

    def get_cols(path):
        with open(path, 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=get_delimiter(path, 4096))
            return next(data)

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # if os.listdir(UPLOAD_FOLDER):
    files = list()
    st.subheader("Archivos Guardados:")

    for file_name in os.listdir(UPLOAD_FOLDER):
        # if file_name.endswith(".csv"):
        files.append(file_name)

    # conn = sqlite3.connect("database/archivos.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT direccion, etiqueta FROM archivos")
    # archivos = cursor.fetchall()
    # conn.close()

    # if archivos:
        # st.write("Archivos guardados:")
        # for file_path, label in archivos:
            # file_name = os.path.basename(file_path)

            # col1, col2, col3 = st.columns(3)

    seleccion = st.selectbox(label="Seleccionar Archivo:", options=files)
    path = os.path.join(f'Data/{seleccion}')
    archivo = pd.read_csv(path, delimiter=get_delimiter(path, 4096))

    st.divider()

    archivo

    st.divider()

    seleccion_var_ind = st.selectbox("Seleccionar Variable Independiente:", get_cols(path))
    seleccion_var_dep = st.selectbox("Seleccionar Variable Dependiente:", get_cols(path))

    if seleccion_var_ind != seleccion_var_dep:
        st.line_chart(archivo, x=seleccion_var_ind, y=seleccion_var_dep, height=300)

    st.divider()

    if seleccion == "materia_prima.csv" and seleccion_var_dep == "Precio_carne_res":
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

    elif seleccion == "materia_prima.csv" and seleccion_var_dep == "Precio_carne_cerdo":

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
