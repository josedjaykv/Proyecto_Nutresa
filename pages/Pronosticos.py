import streamlit as st
import login
import os
import csv
import pandas as pd

login.generar_login()

if 'usuario' in st.session_state:
    st.header(':orange[Pronosticos]')

    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if os.listdir(UPLOAD_FOLDER):
        files = list()
        st.write("Archivos guardados:")
        for file_name in os.listdir(UPLOAD_FOLDER):
            if file_name.endswith(".csv"):
                files.append(file_name)

    st.write(files)

    def get_delimiter(file_path, bytes = 4096):
        with open(file_path, "r").read(bytes) as data
        sniffer = csv.Sniffer()
        delimiter = sniffer.sniff(data).delimiter
        return delimiter

    archivo_selec = st.selectbox("Seleccionar archivo", files)
    path_archivo = os.path.join(f'uploads/{archivo_selec}')
    archivo = pd.read_csv(path_archivo, delimiter=get_delimiter(path_archivo, 4096))

    archivo

    st.subheader("Combustible flota :orange['Disel']")
    st.line_chart(archivo.set_index('Year-Month'))
