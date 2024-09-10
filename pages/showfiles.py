import streamlit as st
import pandas as pd
import os
import login

login.generar_login()
if 'usuario' in st.session_state:
    st.header(':orange[Archivos]')

# Carpeta donde se almacenan los archivos
UPLOAD_FOLDER = 'uploads'

# Obtener el archivo seleccionado de la URL
query_params = st.query_params
st.write(query_params)
if 'file' in query_params:
    file_name = query_params['file'][0]
    file_path = os.path.join(UPLOAD_FOLDER, file_name)

    st.write(file_name, file_path)
    
    # Cargar el archivo CSV y mostrarlo en un DataFrame
    if os.path.exists(file_path):
        st.title(f"Contenido del archivo: {file_name}")
        df = pd.read_csv(file_path)
        st.dataframe(df)
    else:
        st.error("El archivo no existe.")
else:
    st.error("No se ha seleccionado ningún archivo.")
