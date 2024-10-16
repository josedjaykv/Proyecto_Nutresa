import streamlit as st
import pandas as pd
import os
import csv
import login

login.generar_login()
st.page_link('pages/Banco_de_datos.py', label='Volver', icon=':material/arrow_back_ios:')

if 'usuario' in st.session_state:

    # Función para guardar el dataframe en un archivo Excel
    def save_to_excel(df, file_path):
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

    # Obtener el archivo seleccionado de la URL
    ####################################################
    UPLOAD_FOLDER = 'uploads'
    file_name = st.session_state.get('file', None)
    if file_name:
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
    else:
        st.error("No se ha seleccionado ningún archivo.")

    st.header(f'Archivo :orange[{file_name}]')

    # Función para obtener el delimitador de un archivo CSV
    ####################################################
    def get_delimiter(file_path, bytes=4096):
        file_extension = os.path.splitext(file_path)[-1]
        if file_extension == '.csv':
            with open(file_path, 'r') as csv_file:
                data = csv_file.read(bytes)  # Lee 4096 bytes del archivo
                delimiter = csv.Sniffer().sniff(data).delimiter
                return delimiter
        elif file_extension == '.xlsx':
            return None

    st.session_state['delimitado'] = get_delimiter(file_path)

    # Obtener el archivo seleccionado de la URL
    ####################################################
    if 'file' in st.session_state:
        # Cargar el archivo según el tipo de extensión
        if os.path.exists(file_path):
            file_extension = os.path.splitext(file_path)[-1]

            if file_extension == '.csv':
                if 'delimitado' not in st.session_state:
                    df = pd.read_csv(file_path, delimiter=',')
                    edited_df = st.data_editor(df, num_rows='dynamic')
                else:
                    df = pd.read_csv(file_path, delimiter=st.session_state['delimitado'])
                    edited_df = st.data_editor(df, num_rows='dynamic')
            
            elif file_extension == '.xlsx':
                df = pd.read_excel(file_path)
                edited_df = st.data_editor(df, num_rows='dynamic')

            # Botón para guardar los cambios
            if st.button("Guardar cambios"):
                if file_extension == '.csv':
                    edited_df.to_csv(file_path, index=False)
                elif file_extension == '.xlsx':
                    save_to_excel(edited_df, file_path)
                                    
                st.success(f"Los cambios en {file_name} se han guardado exitosamente.")
        else:
            st.error("El archivo no existe.")
    else:
        st.error("No se ha seleccionado ningún archivo.")
