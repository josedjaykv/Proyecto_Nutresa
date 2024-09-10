import streamlit as st
import login

st.header('Pagina de :orange[inicio]')
login.generar_login()
if 'usuario' in st.session_state:
    st.subheader('Informacion pagina principal')
