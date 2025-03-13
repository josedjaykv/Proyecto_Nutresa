import sqlite3
import streamlit as st
import pandas as pd
from Home import generarMenu

st.set_page_config(layout="wide")
def validarUsuario(user, password):
    import bcrypt
    
    conn = sqlite3.connect("database/archivos.db")
    cursor = conn.cursor()

    # Buscar el usuario en la base de datos
    cursor.execute("SELECT password FROM usuarios WHERE usuario = ?", (user,))
    row = cursor.fetchone()
    conn.close()

    # Si el usuario existe, verificar la contraseña
    if row:
        stored_password = row[0]  # Contraseña almacenada en la BD
        return bcrypt.checkpw(password.encode(), stored_password.encode())

    return False

def generar_login():
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario'])
    else:
        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuario')
            parPassword = st.text_input('Password', type='password')
            btnLogin = st.form_submit_button('Login', type='primary')
            
            if btnLogin:
                if validarUsuario(parUsuario, parPassword):
                    st.session_state['usuario'] = parUsuario
                    st.rerun()
                else:
                    st.error('Usuario o password incorrectos')