import streamlit as st
import pandas as pd

def generarMenu(usuario):
    with st.sidebar:
        st.image("logoEIA.png", width=100)
        dfusuarios= pd.read_csv('usuarios.csv')
        dfUsuario = dfusuarios[dfusuarios['usuario']==usuario]
        nombre = dfUsuario['nombre'].values[0]
        st.subheader(f'Bienvenido, {nombre}')        

        st.page_link('inicio.py',label='Inicio', icon=':material/home:')
        st.subheader('Tableros')
        st.page_link('pages/Banco_de_datos.py',label='Banco de datos', icon=':material/account_balance:')
        st.page_link('pages/Analisis_de_costos.py',label='Analisis de costos', icon=':material/attach_money:')
        st.page_link('pages/Analisis_de_escenarios.py',label='Analisis de escenarios', icon=':material/emergency:')
        st.page_link('pages/Pronosticos.py',label='Pronosticos', icon=':material/online_prediction:')

        btnSalir = st.button('Salir', type = "primary")
        st.divider()
        if btnSalir:
            st.session_state.clear()    
            st.rerun()