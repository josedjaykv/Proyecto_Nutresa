import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
from Home import generarMenu

def validarUsuario(user, password):
    dfusuarios= pd.read_csv('usuarios.csv')
    if len(dfusuarios[(dfusuarios['usuario']==user) & (dfusuarios['password']==password)])>0:
        return True
    else:
        return False
    
def generar_login():
    if 'usuario' in st.session_state:
        generarMenu(st.session_state['usuario'])
    else:
        with st.form('frmLogin'):
            parUsuario = st.text_input('Usuario')
            parPassword = st.text_input('Password', type='password')
            btnLogin = st.form_submit_button('Login',type='primary')
            if btnLogin:
                if validarUsuario(parUsuario, parPassword):
                    st.session_state['usuario'] = parUsuario
                    st.rerun()
                else:
                    st.error('Usuario o password incorrectos')