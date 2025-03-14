import streamlit as st
import pandas as pd
import os
import sqlite3
import login
from database.db_manager import initialize_database

# Iniciar sesión
login.generar_login()

if 'usuario' in st.session_state:
    initialize_database()
    st.header('Banco de :orange[datos]')

    # Crear una carpeta para almacenar los archivos cargados
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    # Colores para las etiquetas según el riesgo
    risk_colors = {
        'Riesgo regulatorio': 'orange',
        'Riesgo tecnológico': 'blue',
        'Riesgo de mercado': 'red',
        'Sin etiqueta': 'gray'
    }


    # Funciones
    ##################################################################################

    # Función para redirigir
    def redirect_to_showfile(file_name):
        st.session_state['file'] = file_name
        st.session_state['user'] = st.session_state['usuario'] # Para mantener en sesión al usuario
        st.switch_page('pages/showfiles.py')


    # Lógica
    ##################################################################################

    # Se cargan multiples archivos
    uploaded_files = st.file_uploader(
        "Cargar Archivos CSV o Excel", accept_multiple_files=True, type=['csv', 'xlsx']
    )

    #######################
    # Se hace la copia de los archivos luego de cargarlos
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            print(file_path)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Guardar el archivo cargado en el estado
            st.session_state['selected_file'] = uploaded_file.name
            st.session_state['selected_file_path'] = file_path

            # Mostrar un cuadro de selección de etiqueta después de subir el archivo
            st.session_state['show_label_select'] = True

    ###################### Mejorar esta parte para que se vea mejor
    # Luego de que se carga el archivo se selecciona la etiqueta del archivo
    if 'show_label_select' in st.session_state and st.session_state['show_label_select']:
        st.switch_page('pages/Seleccionar_etiquetas.py')


    # Mostrar archivos guardados con sus etiquetas y colores desde la base de datos
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()
    cursor.execute("SELECT direccion, etiqueta FROM archivos")
    archivos = cursor.fetchall()
    conn.close()

    st.session_state

    if archivos:
        st.write("Archivos guardados:")
        for file_path, label in archivos:
            file_name = os.path.basename(file_path)
            color = risk_colors.get(label, 'gray')

            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button(f"Ver {file_name}", key=f"Ver_{file_name}"):
                    redirect_to_showfile(file_name)
            with col2:
                st.markdown(f"<span style='color:{color}; font-weight:bold;'>{label}</span>",
                            unsafe_allow_html=True)
                


