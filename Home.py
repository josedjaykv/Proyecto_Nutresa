import streamlit as st
import sqlite3

def generarMenu(usuario):
    with st.sidebar:
        st.image("logoEIA.png", width=100)
        
        # Conectar a la base de datos y obtener el nombre del usuario
        conn = sqlite3.connect("database/archivos.db")
        cursor = conn.cursor()
        cursor.execute("SELECT nombre FROM usuarios WHERE usuario = ?", (usuario,))
        row = cursor.fetchone()
        conn.close()

        # Si el usuario existe, mostrar su nombre
        if row:
            nombre = row[0]
            st.subheader(f'Bienvenido, {nombre}')
        else:
            st.subheader('Bienvenido')

        # Menú de navegación
        st.page_link('inicio.py', label='Inicio', icon=':material/home:')
        st.subheader('Tableros')
        st.page_link('pages/Banco_de_datos.py', label='Banco de datos', icon=':material/account_balance:')
        st.page_link('pages/Analisis_de_costos.py', label='Analisis de costos', icon=':material/attach_money:')
        st.page_link('pages/Analisis_de_escenarios.py', label='Analisis de escenarios', icon=':material/emergency:')
        st.page_link('pages/Pronosticos.py', label='Pronosticos', icon=':material/online_prediction:')

        #Administrador de usuarios solo para el usuario admin
        if usuario == 'admin':
            st.subheader('Administración')
            st.page_link('pages/Admin_usuarios.py', label='Gestión de usuarios', icon=':material/admin_panel_settings:')


        # Botón de salir
        btnSalir = st.button('Salir', type="primary")
        st.divider()
        if btnSalir:
            st.session_state.clear()
            st.rerun()  