import streamlit as st
import pandas as pd
import os
import login

login.generar_login()
if 'usuario' in st.session_state:
    st.header('Banco de :orange[datos]')
    
# Crear una carpeta para almacenar los archivos cargados
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Cargar múltiples archivos
uploaded_files = st.file_uploader(
    "Cargar Archivos CSV", accept_multiple_files=True, type=['csv']
)

# Función para redirigir
def redirect_to_showfile(file_name):
    st.session_state['file'] = file_name
    st.session_state['user'] = st.session_state['usuario']
    st.switch_page('pages/showfiles.py')

# Guardar los archivos en la carpeta del proyecto
if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Archivo guardado: {uploaded_file.name}")

# Mostrar links para ver el contenido de cada archivo
if os.listdir(UPLOAD_FOLDER):
    st.write("Archivos guardados:")
    for file_name in os.listdir(UPLOAD_FOLDER):
        if file_name.endswith(".csv"):
            if st.button(f"{file_name}"):
                redirect_to_showfile(file_name)



