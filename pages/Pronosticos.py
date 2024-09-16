import streamlit as st
import pandas as pd
import login
import os
import csv

login.generar_login()

if 'usuario' in st.session_state:

    def get_delimiter(file_path, bytes = 4096):
        with open(file_path, 'r') as wrapper:
            sample = wrapper.read(bytes)
            delimiter = csv.Sniffer().sniff(sample).delimiter
            return delimiter
    st.header(':orange[Pronosticos]')

    def get_cols(path):
        with open(path, 'r') as csv_file:
            data = csv.reader(csv_file, delimiter=get_delimiter(path, 4096))
            return next(data)

    UPLOAD_FOLDER = 'uploads'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    if os.listdir(UPLOAD_FOLDER):
        files = list()
        st.write("Archivos Guardados:")

        for file_name in os.listdir(UPLOAD_FOLDER):
            if file_name.endswith(".csv"):
                files.append(file_name)

    seleccion = st.selectbox("Seleccionar Archivo", files)
    path = os.path.join(f'uploads/{seleccion}')
    archivo = pd.read_csv(path, delimiter=get_delimiter(path, 4096))

    archivo

    seleccion_var_ind = st.selectbox("Seleccionar Variable Independiente", get_cols(path))
    seleccion_var_dep = st.selectbox("Seleccionar Variable Dependiente", get_cols(path))

    if seleccion_var_ind != seleccion_var_dep:
        st.line_chart(archivo, x=seleccion_var_ind, y=seleccion_var_dep)
