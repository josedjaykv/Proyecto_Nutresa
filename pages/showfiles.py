import streamlit as st
import pandas as pd
import os
import login

login.generar_login()

st.page_link('pages/Banco_de_datos.py',label='Volver', icon=':material/account_balance:')

file_name = st.session_state['file']

if 'usuario' in st.session_state:
    st.header(f'Archivo :orange[{file_name}]')
    
# Carpeta donde se almacenan los archivos
UPLOAD_FOLDER = 'uploads'

if 'delimitado' not in st.session_state:
    st.session_state['delimitado'] = 'Coma'

# Botón para saber sí es delimitado por punto y coma
st.session_state['delimitado'] = st.radio(
    'El CSV está delimitado por:',
    ['Coma', 'Punto y coma'],
    index=['Coma', 'Punto y coma'].index(st.session_state['delimitado'])
)

# Obtener el archivo seleccionado de la URL
if 'file' in st.session_state:
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    
    # Cargar el archivo CSV y mostrarlo en un DataFrame
    if os.path.exists(file_path):
        st.subheader(f"Contenido del archivo: {file_name}")

        if 'delimitado' not in st.session_state:
            st.session_state['delimitado'] = 'Coma'
        
        if st.session_state['delimitado'] == 'Coma':
            df = pd.read_csv(file_path, delimiter=',')

        if st.session_state['delimitado'] == 'Punto y coma':
            df = pd.read_csv(file_path, delimiter=';')

        st.write(df)
    else:
        st.error("El archivo no existe.")
else:
    st.error("No se ha seleccionado ningún archivo.")
