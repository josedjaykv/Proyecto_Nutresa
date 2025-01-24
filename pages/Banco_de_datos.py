import streamlit as st
import pandas as pd
import os
<<<<<<< HEAD
import login
=======
import sqlite3
import login
from database.db_manager import initialize_database
>>>>>>> a7c2eff (hola)

# Iniciar sesión
login.generar_login()

if 'usuario' in st.session_state:
<<<<<<< HEAD
    st.header('Banco de :orange[datos]')
    
=======
    initialize_database()
    st.header('Banco de :orange[datos]')

>>>>>>> a7c2eff (hola)
    # Crear una carpeta para almacenar los archivos cargados
    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

<<<<<<< HEAD
    # Inicializar diccionario de etiquetas en session_state
    if 'file_labels' not in st.session_state:
        st.session_state['file_labels'] = {}

=======
>>>>>>> a7c2eff (hola)
    # Colores para las etiquetas según el riesgo
    risk_colors = {
        'Riesgo regulatorio': 'orange',
        'Riesgo tecnológico': 'blue',
        'Riesgo de mercado': 'red',
        'Sin etiqueta': 'gray'
    }

    # Función para redirigir
    def redirect_to_showfile(file_name):
        st.session_state['file'] = file_name
        st.session_state['user'] = st.session_state['usuario']
        st.switch_page('pages/showfiles.py')

<<<<<<< HEAD
=======
    # Función para guardar archivo y etiqueta en la base de datos
    def save_to_db(file_path, label):
        conn = sqlite3.connect("database/archivos.db")
        cursor = conn.cursor()

        # Insertar archivo y etiqueta
        cursor.execute("INSERT INTO archivos (direccion, etiqueta) VALUES (?, ?)", (file_path, label))
        conn.commit()
        conn.close()

>>>>>>> a7c2eff (hola)
    # Cargar múltiples archivos
    uploaded_files = st.file_uploader(
        "Cargar Archivos CSV o Excel", accept_multiple_files=True, type=['csv', 'xlsx']
    )

    # Mostrar un "pop-up" de selección de etiqueta al cargar un archivo
    if uploaded_files:
        for uploaded_file in uploaded_files:
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Guardar el archivo cargado en el estado
            st.session_state['selected_file'] = uploaded_file.name
<<<<<<< HEAD
=======
            st.session_state['selected_file_path'] = file_path
>>>>>>> a7c2eff (hola)

            # Mostrar un cuadro de selección de etiqueta después de subir el archivo
            st.session_state['show_label_select'] = True

    # Si hay un archivo cargado y se debe seleccionar una etiqueta
    if 'show_label_select' in st.session_state and st.session_state['show_label_select']:
        st.write(f"Seleccionar etiqueta de riesgo para el archivo: {st.session_state['selected_file']}")
        label = st.selectbox("Etiqueta de riesgo:", 
                             ['Riesgo regulatorio', 'Riesgo tecnológico', 'Riesgo de mercado'], key='label_select')

        # Cuando se confirma la etiqueta, desaparecer el selector
        if st.button('Confirmar etiqueta'):
<<<<<<< HEAD
            # Guardar la etiqueta en el estado
            st.session_state['file_labels'][st.session_state['selected_file']] = label

            # Mostrar el mensaje combinado
=======
            # Guardar en la base de datos
            save_to_db(st.session_state['selected_file_path'], label)

>>>>>>> a7c2eff (hola)
            st.success(f"Archivo guardado: {st.session_state['selected_file']} - "
                       f"Etiqueta '{label}' asignada al archivo.")

            # Hacer que desaparezca el selector de etiqueta
            st.session_state['show_label_select'] = False

<<<<<<< HEAD
    # Mostrar archivos guardados con sus etiquetas y colores
    if os.listdir(UPLOAD_FOLDER):
        st.write("Archivos guardados:")
        for file_name in os.listdir(UPLOAD_FOLDER):
            label = st.session_state['file_labels'].get(file_name, 'Sin etiqueta')
=======
    # Mostrar archivos guardados con sus etiquetas y colores desde la base de datos
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    cursor.execute("SELECT direccion, etiqueta FROM archivos")
    archivos = cursor.fetchall()
    conn.close()

    if archivos:
        st.write("Archivos guardados:")
        for file_path, label in archivos:
            file_name = os.path.basename(file_path)
>>>>>>> a7c2eff (hola)
            color = risk_colors.get(label, 'gray')

            # Mostrar el archivo con su etiqueta coloreada
            st.markdown(f"<span style='color:{color}; font-weight:bold;'>{label}</span> - {file_name}",
                        unsafe_allow_html=True)
            if st.button(f"Ver {file_name}"):
                redirect_to_showfile(file_name)
