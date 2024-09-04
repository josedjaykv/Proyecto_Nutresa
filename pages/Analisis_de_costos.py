import streamlit as st
import login

login.generar_login()
if 'usuario' in st.session_state:
    st.header('Analisis de :orange[costos]')