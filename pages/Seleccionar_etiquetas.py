import streamlit as st
import sqlite3

# Función para guardar archivo y etiqueta en la base de datos
def save_to_db(file_path, label):
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    # Insertar archivo y etiqueta
    cursor.execute("INSERT INTO archivos (direccion, etiqueta) VALUES (?, ?)", (file_path, label))
    conn.commit()
    conn.close()
    
##############
st.write(f"Seleccionar etiqueta de riesgo para el archivo: {st.session_state['selected_file']}")
label = st.selectbox("Etiqueta de riesgo:", 
                        ['Riesgo regulatorio', 'Riesgo tecnológico', 'Riesgo de mercado'], key='label_select')

# Cuando se confirma la etiqueta, desaparecer el selector
if st.button('Confirmar etiqueta'):
    # Guardar en la base de datos
    save_to_db(st.session_state['selected_file_path'], label)

    st.success(f"Archivo guardado: {st.session_state['selected_file']} - "
                f"Etiqueta '{label}' asignada al archivo.")

    # Hacer que desaparezca el selector de etiqueta
    st.session_state['show_label_select'] = False
    
    st.switch_page('pages/Banco_de_datos.py')


